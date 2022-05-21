import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #creating the variable city.
    city = input("Type the name of your city [chicago, new york city, washington] : \n").lower()  
    #using a while loop to verify user input
    while True:
        if city in CITY_DATA.keys():
          break
        else:
          print('wrong input')
          city = input("Type the name of your city [chicago, new york city, washington] : \n").lower()  

    #Creating a list of months(january,february,...,all)
    months = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Pick a month (all, jan, feb, ... , jun): \n").lower()
    #using a while loop to verify user input
    while month not in months:
          print('Wrong input')
          month = input("Pick a month (all, jan, feb, ... , jun): \n").lower()
    #Creating a list of days(monday,tuesday,friday,....,all)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saterday', 'sunday']
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Pick a day (all, monday, tuesday, ..., sunday):\n').lower()
    #using a while loop to verify user input
    while day not in days:
         print('Wrong input')
         day = input('Pick a day (all, monday, tuesday, ..., sunday):\n').lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns                                     
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    
    months = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']  
    # filter by month if applicable
    if month != 'all':
       months.pop(0)
       # use the index of the months list to get the corresponding int
       month = months.index(month) + 1
       # filter by month to create the new dataframe
       df = df[df['month'] == month]
                                         
    # filter by day of week if applicable
    if day != 'all':
       # filter by day of week to create the new dataframe
       df = df[df['day_of_week'] == day.title()]

                                         
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m_c_m = df['month']
    print('The most common month: ',m_c_m.mode()[0])

    # TO DO: display the most common day of week
    m_c_d = df['day_of_week']
    print('The most common day: ', m_c_d.mode()[0])

    # TO DO: display the most common start hour
    m_c_sh = df['start_hour']
    print('The most common start hour: ', m_c_sh.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    c_s_s = df['Start Station'].mode()[0]
    print('The most common start station: {}'.format(c_s_s))

    # TO DO: display most commonly used end station
    c_e_s = df['End Station'].mode()[0]
    print('The most common end station: {}'.format(c_e_s))

    # TO DO: display most frequent combination of start station and end station trip
    df['path']=df['Start Station']+","+df['End Station']
    path = df['path'].mode()[0]
    print('The most common path: {}'.format(path))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    t_t_t = df['Trip Duration'].sum().round()
    print('Total travel time: ',t_t_t)

    # TO DO: display mean travel time
    m_t_t = df['Trip Duration'].mean().round()
    print('Mean travel time: ',m_t_t)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts().to_frame()
    print("Counts of user types: {}".format(user_type))

    # TO DO: Display counts of gender
    if city != 'washington':
        user_gender = df['Gender'].value_counts().to_frame()
        print("Counts of gender: {}".format(user_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
        e_b_y = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth: ',e_b_y)
          
        m_r_y = int(df['Birth Year'].min())
        print('Most recent year of birth: ',m_r_y)
          
        m_c_y = int(df['Birth Year'].max())
        print('Most common year of birth: ',m_c_y)
    else:
        print("No thing to display!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('\nRaw data in available to check. \n')
    
    index = 0
    user_input = input('would you like to diplay more? , please type y or n ').lower()
    #creating while loop to ensure the correct user input
    while True:
        if user_input == 'n':
            print('Thank You')
            break
        elif user_input == 'y' and index + 5 < df.shape[0]: 
               print(df.iloc[index:index+5])
               index += 5
               user_input = input('would you like to diplay more? , please type y or n ').lower()
               if user_input != 'y':
                  print('Ending')
                  break
        else:   
              print('Wrong input')
              user_input = input('would you like to diplay more? , please type y or n ').lower() 
              if user_input == 'n':
                 print('Thank You')
                 break        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
