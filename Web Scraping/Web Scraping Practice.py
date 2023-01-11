from bs4 import BeautifulSoup
import requests
import csv
html_text = requests.get('https://realpython.github.io/fake-jobs/').text
soup = BeautifulSoup(html_text, 'lxml')
job_elements = soup.find_all('div', class_='card-content')
with open('D:\Python cơ bản\Python_Fundamental\Web Scraping\job.csv', 'w',newline='') as f:
    csvwriter = csv.writer(f)
    fields = ['Title', 'Company', 'Location', 'Link detail', 'Link apply']
    csvwriter.writerow(fields)
    for job_element in job_elements:
        title_element = job_element.find('h2', class_ ='title is-5').text.strip()
        if 'python' in title_element.lower():
            company_element = job_element.find('h3', class_='subtitle is-6 company').text.strip()
            location_element = job_element.find('p', class_='location').text.strip()
            info = [title_element, company_element, location_element]
            links = job_element.find_all('a')
            for link in links:
                link_url = link['href']
                info.append(link_url)
            csvwriter.writerow(info)

# python_jobs = soup.find_all('h2', string=lambda text:'python' in text.lower())
# python_jobs_elements = [i.parent.parent.parent for i in python_jobs]
# for python_jobs_element in python_jobs_elements: 
#     title_element = python_jobs_element.find('h2', class_ ='title is-5').text.strip()
#     company_element = python_jobs_element.find('h3', class_='subtitle is-6 company').text.strip()
#     location_element = python_jobs_element.find('p', class_='location').text.strip()
#     print(title_element)
#     print(company_element)
#     print(location_element)
    