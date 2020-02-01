import time
import pandas as pd
import numpy as np
#Dictionary of csv file we will use
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
    city = ''
    month = ''
    day = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while not city in CITY_DATA.keys():
        city = input('What is the name of the city you would like to analyze chicago, new york city or washington\n')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']
    while not month in month_list:
        month = input("Please select a month all, january, february, ... , june\n")
    if month != 'all':
        month = month_list.index(month)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_in_week = ['all', 'monday','sunday','tuesday','wednesday','thursday', 'friday', 'saturday']
    while day not in days_in_week:
        day = input("Please select a day of the week all, monday, tuesday, ... sunday\n")
    
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all': 
        df = df.query('month == 1'.format(month))
   
    if day != 'all':
        df = df.query('day_of_week == "{}"'.format(day.title()))
    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == "all":
        month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']
        most_common_month_index = df['month'].mode()[0]
        month_name = month_list[most_common_month_index]
        print("The month {} had the most travel is {}\n".format(city, month_name.title()))

    # TO DO: display the most common day of week
    if day == "all":
        print("The day {} had the most travel is {}\n".format(city, df['day_of_week'].mode()[0]))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The hour {} has the most travel was {}".format(city, df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common used start station for {} was {}\n".format(city, df['Start Station'].mode()[0]))    

    # TO DO: display most commonly used end station
    print("The most common used end station for {} was {}\n".format(city, df['End Station'].mode()[0]))    

    # TO DO: display most frequent combination of start station and end station trip
    n_combos = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of  in {} was \n{}\n'.format(city,n_combos))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time for {} was {} minutes".format(city,df['Trip Duration'].sum() / 60 ))

    # TO DO: display mean travel time
    print('The average travel time for {} was {} minutes'.format(city, df['Trip Duration'].mean()/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertypes = df.groupby('User Type')['User Type'].count()
    print('The count of each type of user in {} is \n{}\n'.format(city, usertypes))
    if 'Gender' in df.columns:
        # TO DO: Display counts of gender
        gendertypes = df.groupby('Gender')['Gender'].count()
        print('The count of each gender in {} are \n{}\n'.format(city, gendertypes))
    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        print('In {} \nthe most common year of birth was {}\nthe most recent year of birth was {}\nthe most recent year of birth was {}\n'
            .format(city, df['Birth Year'].mode()[0], df['Birth Year'].max(), df['Birth Year'].min()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,city, month, day)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
          


if __name__ == "__main__":
	main()
