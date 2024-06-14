# Generation Identifier and Explainer
try:
    myGeneration = int(input("In which year did you breathe the first time? "))
    if 1883 <= myGeneration <= 1900:
        print("Lost Generation (1883-1900): They were disoriented, wandering, and directionless following the devastating effects of World War I. Known for a sense of existential angst and disillusionment.")
    elif 1901 <= myGeneration <= 1927:
        print("Greatest Generation (1901-1927): They grew up during the Great Depression and fought in World War II. Known for their sense of duty, work ethic, and perseverance.")
    elif 1928 <= myGeneration <= 1945: 
        print("Silent Generation (1928-1945): They were children during the Great Depression and World War II. Known for their cautious approach, discipline, and valuing traditional values.")
    elif 1946 <= myGeneration <= 1964:
        print("Baby Boomers (1946-1964): They were born post-World War II during a time of significant population increase. Known for their optimism, sense of entitlement, and strong work ethic.")
    elif 1965 <= myGeneration <= 1980:
        print("Generation X (1965-1980): They grew up during a time of shifting societal values and were often left alone as children (latchkey kids). Known for their independence, skepticism, and resourcefulness.")
    elif 1981 <= myGeneration <= 1996:
        print("Millennials (1981-1996): They grew up during the rise of technology and witnessed significant economic changes. Known for their tech-savviness, value for diversity, and tendency to seek purpose in their work.")
    elif 1997 <= myGeneration <= 2012:
        print("Generation Z (1997-2012): They have grown up with the internet and social media as integral parts of their lives. Known for their digital nativeness, social awareness, and entrepreneurial spirit.")
    elif 2013 <= myGeneration <= 2024:
        print("Generation Alpha (2013-2024): They are growing up in a highly digital and connected world. Predicted to be highly tech-savvy, educated, and immersed in technology from a very young age.")
    else:
        print("Year out of defined generation range")
except ValueError:
    print("Invalid input. Please enter a valid year.")
