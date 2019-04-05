#!/usr/bin/python
import requests, os, getopt, sys, json, datetime


def extract_urls(inputfile,outputfile):
    list = []
    print("[!] Reading TXT: "+inputfile)
    with open(inputfile,"rU") as fp:
        for line in fp:
            if "http://" in line or "https://" in line:
                data = line.replace("\n","").replace("\r","").replace("\t","")
                list.append(data)
    if len(list) > 0:
        res = ""
        for l in list:
            res += l+"\n"
            print("[+] "+l)

        with open(outputfile, 'a') as the_file:
            print("[!] Writing output: "+outputfile)
            the_file.write(str(res))
        print("[!] Process completed!")
    else:
        print("Nothing to export!")

def main(argv):
    helpstr = os.path.basename(__file__)+' -f input.txt -o output.txt'
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hf:o:",["txt=","output="])
    except getopt.GetoptError:
        print(helpstr)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpstr)
            sys.exit()
        elif opt in ("-f", "--txt"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
    if inputfile != "" and os.path.isfile(inputfile) and outputfile != "":
        extract_urls(inputfile,outputfile)
    else:
        print(helpstr)

if __name__ == "__main__":
    main(sys.argv[1:])
