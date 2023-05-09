import speedtest


st = speedtest.Speedtest()

print(f"Your ping is: {st.results.ping} ms")
print(f"download speed is {round(st.download()/1000000/1)} Mbps")
#print(st.download())
print(f"\n upload speed is {round(st.upload()/1000000)} Mbps")



# Method 2
#import pyspeedtest
#st = pyspeedtest.SpeedTest()
#st.ping()
#st.download()
#st.upload()
