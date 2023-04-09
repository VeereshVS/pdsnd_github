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
    city = input("Select the City you want to analyse the data for, Please choose from -> chicago, new york city, washington \n").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("Oops!! Entered city is not supported", city)
        city = input("Please Select the City from -> chicago, new york city, washington \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Select the Month you want to analyse the data for, Please choose from -> all, january, february, march, april, may, june \n").lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("Oops!! Entered Month is not supported", month)
        month = input("Please Select the Month from -> all, january, february, march, april, may, june \n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Select the Day you want to analyse the data for, Please choose from -> all, monday, tuesday, wednesday, thursday, friday, saturday, sunday \n").lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("Oops!! Entered Day is not supported", day)
        month = input("Please Select the Day from -> all, monday, tuesday, wednesday, thursday, friday, saturday, sunday \n").lower()

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
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    print("Most common month of usage", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Most common Day of usage", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("Most common Start Hour of usage", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most commonly used end station", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Stations'] = df[['Start Station', 'End Station']].apply(lambda x: '-'.join(x), axis=1)
    print("Most frequent combination of start station and end station trip", df['Start End Stations'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time", df["Trip Duration"].sum())

    # TO DO: display mean travel time
    print("Mean travel time", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types", df["User Type"].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("counts of gender", df["Gender"].value_counts())
    else:
        print("'Gender' data doesn't exists in current city data selected")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest Year of birth", df["Birth Year"].min())
        print("Most Recent Year of birth", df["Birth Year"].max())
        print("Most Common Year of birth", df["Birth Year"].mode()[0])
    else:
        print("'Birth Year' data doesn't exists in current city data selected")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays Raw Data in bikeshare data"""
    print(df.shape[0])
    iter_count = 0
    while True:
        display = input('\nWould you like to See the Raw Bikehare Data? Enter yes or no.\n')
        if display == 'yes':
            if iter_count < 1:
                print("First 5 rows of Bikeshare Data -> \n")            
            else:
                print("Next 5 rows of Bikeshare Data -> \n")
            if iter_count+5 <= df.shape[0]:
                print(df[iter_count:iter_count+5])
            else:
                print(df[iter_count:])
            iter_count += 5     
        else:
            break


def main():
    while True:
        # Get Inputs from User
        city, month, day = get_filters()
        # Load the Data as per user prompts
        df = load_data(city, month, day)

        # Display statistics on the most frequent times of travel
        time_stats(df)
        # Display statistics on the most popular stations and trip
        station_stats(df)
        # Display statistics on the total and average trip duration
        trip_duration_stats(df)
        # Display statistics on bikeshare users
        user_stats(df)

        # Display Raw Data from Bikeshare data 
        display_raw_data(df)

        # Ask for User prompt for restart the report generation
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
