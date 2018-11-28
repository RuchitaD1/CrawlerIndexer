import pandas as pd
import bs
import csv
def retSeeds():

    seeds=[u"https://www.epicurious.com"
           ]

    writeFile=open('new.csv', 'a')
    writer = csv.writer(writeFile)
    writer.writerow(['inlink','link','outlink'])
    import requests
    ols={}
    cnt=0

    for seed in seeds:
        #if(cnt<=5):


            try:
                request = requests.get(seed)
                if request.status_code == 200:
                    print "parsing" + seed
                    outlinks = bs.scape(seed)
                    cnt += 1




                    if seed in ols:
                        inlink=ols[seed]
                    else:
                        inlink="Seed"
                    row=[seed,inlink,outlinks]
                    for outlink in outlinks:
                        #print "outlink:",outlink
                        ols[outlink]=seed
                        #row=[inlink,seed,outlink]
                        if str(outlink).startswith('http')==True:
                            if outlink not in seeds:
                                seeds.append(outlink.decode('utf-8'))

                    #writer.writerow(row)
                    print "cnt:",cnt

                #print raw_data
        #writeFile.close()
        #df=pd.read_csv('new.csv')
            except:
                print "Error"
    print "Total parsed:"+str(cnt)
    print len(seeds)
    return seeds
