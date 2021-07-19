import setuptools

setuptools.setup(
    name = "RNPDNO Scrapper",
    version = "1.0.0",
    description = "A Python-based scrapper to extract data from the public version of the RNPDNO",
    author = "Pablo Reyes Moctezuma",
    author_email = "pablo.reyes.moctezuma@gmail.com",
    url = "https://github.com/pablorm296/ScrapperRNPDNO",
    license = "GNU General Public License v3.0.",
    keywords = ["Mexico", "scrapping", "web scrapping", "requests"],
    packages = ["RNPDNO_Scrapper"],
    package_dir = {
        "RNPDNO_Scrapper": "RNPDNO_Scrapper"
    }
)