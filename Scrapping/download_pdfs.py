# write code to download pdfs from provided urls
import requests
import os
import urllib.request
import tqdm

english_pdfs=[
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hotels-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/exempted-structural-standards-hotels-en-v011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/serviced-apartment-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/exempted-structural-standards-serviced-apartment-en-v011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/camps-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/chalets-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hostels-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/apartments-hotel-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/resorts-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hotel-villas-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/popup-accommodations-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/heritage-hotels-classification-criteria-en-v02.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Hospitality-Facilities-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Hospitality-Facilities-Regulations-service-directory-En-V014.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Private-Hospitality-Facility-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Private-Hospitality-Facility-Regulations-service-directory-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Travel-and-Tourism-Services-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Travel-and-Tourism-Services-Regulations-service-directory-En-V014.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tour-Guide-Regulations-En-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Tour-Guide-Regulations-service-directory-En-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Management-of-Hospitality-Facilities-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Management-of-Hospitality-Facilities-Regulations-service-directory-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Experimental-Sectors-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Experimental-Sectors-Regulations-service-directory-En-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Consultation-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Tourism-Consultation-Regulations-service-directory-En-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Saudi-Tourism-Regulation-En-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Hospitality-Facilities-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Management-of-Hospitality-Facilities-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Travel-and-Tourism-Services-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tour-Guide-Regulations-En-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Private-Hospitality-Facility-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Consultation-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Experimental-Sectors-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Inspection-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Violations-Committee-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Activities-Inspection-Regulation-Procedures-Guide-En-V01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Development-of-Tourism-Destinations-Regulations-En-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourist-Visa-Regulations-En-V012.pdf",   
]

arabic_pdfs=[
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hotels-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hotels-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hotels-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/specialty-types-of-hotels-ar-v011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/specialty-types-of-hotels-ar-v011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/exempted-structural-standards-hotels-ar-v012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/serviced-apartment-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/exempted-structural-standards-serviced-apartment-ar-v012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/camps-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/chalets-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hostels-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/apartments-hotel-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/resorts-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/hotel-villas-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/popup-accommodations-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/classification-criteria/heritage-hotels-classification-criteria-ar-v01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Hospitality-Facilities-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Hospitality-Facilities-Regulations-service-directory-Ar-V014.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Private-Hospitality-Facility-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Private-Hospitality-Facility-Regulations-service-directory-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Travel-and-Tourism-Services-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Travel-and-Tourism-Services-Regulations-service-directory-Ar-V014.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tour-Guide-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Tour-Guide-Regulations-service-directory-Ar-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Management-of-Hospitality-Facilities-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Management-of-Hospitality-Facilities-Regulations-service-directory-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Experimental-Sectors-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Experimental-Sectors-Regulations-service-directory-Ar-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Consultation-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/services-directory/Tourism-Consultation-Regulations-service-directory-Ar-V013.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Saudi-Tourism-Regulation-Ar-V014.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Hospitality-Facilities-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Management-of-Hospitality-Facilities-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Travel-and-Tourism-Services-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tour-Guide-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Private-Hospitality-Facility-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Consultation-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Experimental-Sectors-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Inspection-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Violations-Committee-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Activities-Inspection-Regulation-Procedures-Guide-Ar-V01.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Development-of-Tourism-Destinations-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourist-Visa-Regulations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Hospitality-Facilities-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Hospitality-Facilities-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Private-Hospitality-Facility-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Private-Hospitality-Facility-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Travel-and-Tourism-Services-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Travel-and-Tourism-Services-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Experimental-Sectors-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Experimental-Sectors-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Consultation-Violations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tourism-Consultation-Violations-Ar-V012.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tour-Guide-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Tour-Guide-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Management-of-Hospitality-Facilities-Violations-Ar-V011.pdf",
    "https://cdn.mt.gov.sa/mtportal/mt-fe-production/content/policies-regulations/documents/tourism-regulations/Management-of-Hospitality-Facilities-Violations-Ar-V011.pdf",
]

# check if the directory exists
if not os.path.exists("english_pdfs"):
    os.makedirs("english_pdfs")
    
if not os.path.exists("arabic_pdfs"):
    os.makedirs("arabic_pdfs")
    
print("Downloading English PDFs")
progress = tqdm.tqdm(range(len(english_pdfs)))
for idx,pdf in enumerate(english_pdfs):
    progress.set_description("Downloading English PDFs")
    response = requests.get(pdf)
    with open("english_pdfs/"+pdf.split("/")[-1], 'wb') as f:
        f.write(response.content)
        progress.update(1)
    
    
print("Downloading Arabic PDFs")
progress = tqdm.tqdm(range(len(arabic_pdfs)))
for idx,pdf in enumerate(arabic_pdfs):
    progress.set_description("Downloading Arabic PDFs")
    response = requests.get(pdf)
    with open("arabic_pdfs/"+pdf.split("/")[-1], 'wb') as f:
        f.write(response.content)
        progress.update(1)
        