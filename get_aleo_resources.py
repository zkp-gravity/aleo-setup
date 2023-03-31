import gdown

url = "https://drive.google.com/drive/folders/1MxnsQ8sGGA_dPv_u2j85URDU4pqgTocg"
gdown.download_folder(url, quiet=False, use_cookies=False)

