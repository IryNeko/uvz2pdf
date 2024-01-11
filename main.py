'''
convert uvz file to pdf image file

zipfile
'''
import zipfile
import sys
import img2pdf
import os

def uvz_unzip(path):
    with zipfile.ZipFile(path, 'r') as myzip:
        myzip.extractall("tmp/")
    print("file extracted successfully")
    return True
def dpg_to_pdf(path):
    list=os.listdir("tmp")
    path_list=[]
    new_list=[]
    # doing an ordered hit bok,cov,fow,leg,then all the rest
    for i in list:
        if "cov" in i:
            new_list.append("tmp/"+i)
    for i in list:
        if "fow" in i:
            new_list.append("tmp/"+i)
    for i in list:
        if "leg" in i:
            new_list.append("tmp/"+i)
    for i in list:
        if "bok" in i:
            new_list.append("tmp/"+i)
    for i in list:
        if ("cov" in i or "fow" in i or "leg" in i or "bok" in i):
            pass
        else:
            if "pdg" in i:
                new_list.append("tmp/"+i)      
    print("there are",len(new_list),"pages in the book")
    out_path=path.replace(".uvz",".pdf")    
    with open(out_path,"wb") as f:
        f.write(img2pdf.convert(new_list))
    print("converted to pdf,starting cleanup")
    return out_path
def cleanup(): # clean up the tmp folder
    list=os.listdir("tmp")
    for i in list:
        os.remove("tmp/"+i)
    print("clean up complete")
    return True
if __name__=='__main__':
    path=sys.argv[1]
    print(path)
    uvz_unzip(path)
    dpg_to_pdf(path)
    cleanup()
# first unzip the file

# second sew a pdf