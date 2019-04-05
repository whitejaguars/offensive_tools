#!/usr/bin/python
import os, sys, time
from datetime import date
from datetime import datetime

def generate_passwords(targets_file, output_file):
    ptargets = None
    if targets_file != '':
        if os.path.exists(targets_file):
            ptargets = []
            f = open(targets_file)
            line = f.readline()
            #Variants adding numbers
            #Common numbers in passwords first
            common_numbers = ['123','321','234','432','345','543','456','654','567','765','678','876','789','987','890','098','007','911','506']
            #[0-9]
            for x in range(0, 32):
                common_numbers.append(str(x))
            #Adding last 30 years
            for x in range(date.today().year - 30,date.today().year+1):
                common_numbers.append(str(x))

            #Special Chars
            special_chars = ['#','@','$','!','_','%']

            #Passwords count
            totalpass = 0
            totalwords = 0
            started = datetime.now()
            print '[!] Starting process'
            while line:
                t = line.strip().split(',')
                for each_host in t:
                    t2 = each_host.strip().split(';')
                    for each_subhost in t2:
                        t3 = each_subhost.strip().split(':')
                        for p in t3:
                            password = p.strip().replace(' ','')
                            if password.strip() != '':
                                totalwords += 1
                                print '[!] Creating variants for: '+password
                                #Generate variants
                                variants = [password]
                                #First Uppercase char
                                if password[:1].isalpha():
                                    if password[:1].islower():
                                        variant = password[:1].upper() + password[1:]
                                    else:
                                        variant = password[:1].lower() + password[1:]
                                    variants.append(variant)
                                #Numbers
                                for each_variant in variants:
                                    if not hasNumbers(each_variant):
                                        for each_number in common_numbers:
                                            variants.append(each_variant+each_number)
                                            variants.append(each_number+each_variant)
                                        #Replace L33t chars : p@ssw0rd
                                        variant = each_variant.replace('a','@')
                                        if variant not in variants:
                                            variants.append(variant)
                                            variants.append(each_variant.replace('a','4'))

                                        variant = variant.replace('e','3')
                                        if variant not in variants:
                                            variants.append(variant)
                                            variants.append(each_variant.replace('e','3'))

                                        variant = variant.replace('i','1')
                                        if variant not in variants:
                                            variants.append(variant)
                                            variants.append(each_variant.replace('i','1'))

                                        variant = variant.replace('o','0')
                                        if variant not in variants:
                                            variants.append(variant)
                                            variants.append(each_variant.replace('o','0'))

                                        #p1a2s3s4w5o6r7d8
                                        c=1
                                        variant = ''
                                        for each_char in each_variant:
                                            variant += each_char + str(c)
                                            c += 1
                                        variants.append(variant)
                                #Special Characters
                                tmp=[]
                                for each_variant in variants:
                                    for each_char in special_chars:
                                        if not each_char in each_variant:
                                            tmp.append(each_variant+each_char)
                                            tmp.append(each_char+each_variant)
                                for t in tmp:
                                    variants.append(t)

                                #Send all the variants to the output file
                                totalpass += len(variants)
                                print '[!] Current total: '+str(totalpass)+ ' | ' + str(len(variants)) + ' variants made for : ' + password
                                for each_variant in variants:
                                    write(each_variant, output_file)
                line = f.readline()
            f.close()
            completed = datetime.now()
            total_time =  completed - started
            hours, remainder = divmod(total_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            duration_formatted = str(hours)+':'+str(minutes)+':'+str(seconds)
            print '*'*60
            print '[!] Process completed'
            print 'Started at: ' + str(started)
            print 'Completed at: '+ str(completed)
            print 'Elapsed time: '+ str(duration_formatted)
            print 'Initial words:' + str(totalwords)
            print 'Total of variants generated:' + str(totalpass)
            print 'Results stored in: '+output_file
    return ptargets

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def write(data, filename):
    try:
        savefile = open(filename,'a')
        savefile.write(data+'\n')
        savefile.close()
    except Exception, e:
        print '[!] Error:'+str(e)


#Fun start here
if len(sys.argv) == 3:
    if str(sys.argv[1]) != '':
        try:
            input_file = sys.argv[1]
            output_file = sys.argv[2]
            generate_passwords(input_file, output_file)
        except Exception, e:
            print '[!] Error:'+str(e)
else:
    print 'WhiteJaguars Cyber Security'
    print 'This is a simple tool for generating password variants based on initial lists'
    print 'Why?'
    print 'In some cases you may want to try a specific list of possible passwords based'
    print 'on keywords applicable for your target such as name, last name, phone numbers,'
    print 'company based keywords or even dictionaries in other languages'
    print ' '
    print 'Usage:'
    print 'python pass_generator.py input_file output_file'
