import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['saturday', 'sunday' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*40)
    print('\nHello! Let\'s explore some US bikeshare data!')
    print('\nMohamed Salem Ali Code (^_^)\n')
    print('-'*40)
 
    while True:
       try:
           city = input("\nEnter the name of the city (chicago, new york city, washington) :  ").lower()
       except:
           continue

       if city in  CITY_DATA:
           break
       else:
        print("\n(InValid Input)")
    print('-'*40)

    while True:
       try:
           month = input("\nEnter the month number (1,2,3,4,5,6) or all : ").lower()
       except:
           continue

       if month == 'all':
           break
       elif month in {'1', '2', '3', '4', '5', '6'}:
           month = MONTHS[int(month) - 1]
           break
       else:
           print("\n(InValid input)")
           continue

    while True:
        try:
            day = input("\nEnter the Day number (1,2,3,4,5,6,7) or all : ").lower()
        except:    
            continue

        if day == 'all':
            break
        elif day in {'1', '2', '3', '4', '5', '6', '7'}:
            day = WEEKDAYS[int(day) - 1]
            break
        else:
            print("\n(InValid input)")
            continue
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    startTime = time.time()
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month                 
    df['day'] = df['Start Time'].dt.day       
    df['hour'] = df['Start Time'].dt.hour   
    if month != 'all':
        m = MONTHS.index(month) + 1
        df = df[df.month == m]
        month = month.title()
    
    if day != 'all':
        d = WEEKDAYS.index(day)
        df = df[df.day == d]
        day = day.title()
       
    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40,'\n')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    startTime = time.time()
    
   
    #x1=df['month'].mode()[0]-1
    #print(x1)
    #commonMonth1 = MONTHS[x1].title()
    commonMonth2 = df['month'].value_counts().idxmax()
    print('\nthe most common month : ' ,commonMonth2)

    #x2=df['day'].mode()[0]
    #print(x2)
    #commonDay1 = WEEKDAYS[x2].title()
    commonDay2 = df['day'].value_counts().idxmax()
    print('\nthe most common day of week : ' ,commonDay2)


    commonStartHour = df['hour'].mode()[0]
    print('\nthe most common start hourr : ', commonStartHour)


    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    startTime = time.time()


    startStation = df['Start Station'].mode()[0]
    print('\nmost commonly used start station : ', startStation)
    
    endStation = df['End Station'].mode()[0]
    print('\nmost commonly used end station : ', endStation)




    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    startTime = time.time()


    totalTravelTime = int(df['Trip Duration'].sum())
    print('\nTotal travel time : ', totalTravelTime)

    meanTravelTime = int(df['Trip Duration'].mean())
    print('\nMean travel time : ', meanTravelTime)

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    startTime = time.time()

    userTypes = df['User Type'].value_counts()
    for i in range(len(userTypes)):
        value = userTypes[i]
        userType = userTypes.index[i]
        print("\nCount of user types",userType + ' : ', value)

    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        for i in range(len(genders)):
            value = genders[i]
            gender = genders.index[i]
            print("\nCount of gender : ",gender + ' : ', value)
   
 
    if 'Birth Year' in df.columns:
        Min = int(df['Birth Year'].min())
        Max = int(df['Birth Year'].max())
        mostCommon = int(df['Birth Year'].mode())
        print('\nEarliest year of birth : ', Min )
        print('\nMost recent year of birth : ', Max )
        print('\nMost common year of birth : ', mostCommon)

    print("\nThis took %s seconds." % (time.time() - startTime))
    print('-'*40)

def rawData (df):
    print('\npress enter to see row data, press no to skip\n')
    x = 0
    while (input().lower() != 'no'):
        x = x+10
        print(df.head(x))
        print('\npress no to exit  , Enter to continue \n')
def main():
    while True:
        city, month, day = get_filters()
        #print("City::"+city +"\nMonth::"+month+"\nDay::"+day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawData(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
