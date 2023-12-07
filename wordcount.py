#
import sys, os, re
def usage():
   print("Word and Line counter Marjan Karami, Uni Potsdam, 2023")
   print("Usage: appname [-h -clw] filename")
   print("  Options are:")
   print("     -h   - seeing this help page")
   print("     -c   - counting only chars")
   print("     -l   - counting only lines")
   print("     -w   - counting only words")
   print("     -o   - counting only lowercase words")
   print("     -w   - counting only uppercase words")
   exit()
   
def wc (filename):
    counter= { 
    "nlines"  :0,
    "nwords"  :0, 
    "nchars"  :0, 
    "nlow"    :0,
    "nupp"    :0,
    "filename":""
    }

    file = open(filename,'r')
    for line in file: 
       counter["nlines"] +=  1
       counter["nchars"] +=  len(line)
       counter["nwords"] +=  len(line.split())
       counter["nlow"]   += sum(1 for c in line.split() if c.islower())
       counter["nupp"]   += sum(1 for c in line.split() if c.isupper())
    file.close()
    counter["filename"]= filename
    return counter 

def main (args):
    if len(args) == 1 or "-h" in args:
       usage()
       exit()
    print(args)
    word = True
    lines = True
    chars = True
    lowercase=True
    uppercase=True
    if len(args) > 2:
        for arg in args[2:]:
            result = wc(arg)
            word = any((re.search('^-([cwlou])\1?',item)and 'w' in item) for item in list(args))
            lines= any((re.search('^-([cwlou])\1?',item)and 'l' in item) for item in list(args))
            chars= any((re.search('^-([cwlou])\1?',item)and 'c' in item) for item in list(args))
            lowercase = any((re.search('^-([cwlou])\1?',item)and 'o' in item) for item in list(args))
            uppercase = any((re.search('^-([cwlou])\1?',item)and 'u' in item) for item in list(args))

            result_dict = {}
            if lines:
                result_dict['lines'] = result['nlines']
            if word:
                result_dict['words'] = result['nwords']
            if chars:
                result_dict['chars'] = result['nchars']
            if lowercase:
                result_dict['nlow'] = result['nlow']
            if uppercase:
                result_dict['nupp'] = result['nupp']

            result_dict['filename'] = result['filename']
            for key, value in result_dict.items():
                print(f"{value}\t", end="")
            print("")

    else:
        result = wc(args[1])
        result_dict = {}
        if lines:
            result_dict['lines'] = result['nlines']
        if word:
            result_dict['words'] = result['nwords']
        if chars:
            result_dict['chars'] = result['nchars']

        result_dict['filename'] = result['filename']

        for key, value in result_dict.items():
            print(f"{value}\t", end="")
        print("")
if __name__ == "__main__":
   #print(sys.argv)
   main(sys.argv)    
