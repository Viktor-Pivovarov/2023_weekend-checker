from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

def checkWeekend(month, day):
    try:
        day, month = int(day), int(month)
        if not (1 <= month <= 12) or not (1 <= day <= 31):
            return "Invalid input"
    except ValueError:
        return "Invalid input"
    
    months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.consultant.ru/law/ref/calendar/proizvodstvennye/2023/")
        
        cells = driver.find_elements(By.XPATH, f"//td[text()='{day}']")
        
        for cell in cells:
            if cell.find_element(By.XPATH, "ancestor::table").find_element(By.XPATH, "thead//th").text == months[month-1]:
                cell_class = cell.get_attribute('class')
                if any(keyword in cell_class for keyword in ['weekend', 'holiday']):
                    return "Weekend"
                else:
                    return "Working day"
        return "Date not found"
    except WebDriverException as e:
        return f"Error connecting to the server: {e}"
    finally:
        if driver:
            driver.quit()

while True:
    date = input("Enter the date in the format DD.MM: ")
    try:
        day, month = date.split('.')
        result = checkWeekend(month, day)
        if result != "Invalid input":
            print(result)
            break
        else:
            print(result)
    except ValueError:
        print("Invalid date format")
