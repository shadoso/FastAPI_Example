from secrets import password
import psycopg2

HOST_NAME = 'localhost'
DATABASE = 'WOD'
USER_NAME = 'postgres'
PASSWORD = password()
PORT_ID = 5432

database = psycopg2.connect(
    host=HOST_NAME,
    dbname=DATABASE,
    user=USER_NAME,
    password=PASSWORD,
    port=PORT_ID
)
sql = database.cursor()

create_table = '''      CREATE TYPE genders AS ENUM (
                        'F', 'M');
                        
                        CREATE playable AS ENUM (
                        'NPC', 'Player');
                        
                        CREATE traditions AS ENUM (
                        'Akashic Brotherhood',
                        'Celestial Chorus',
                        'Cult of Ecstasy',
                        'Dreamspeakers',
                        'Euthanatos',
                        'Order of Hermes',
                        'Sons of Ether',
                        'Verbena',
                        'Virtual Adepts',
                        'Technocracy');
                        
                        CREATE TYPE martial AS ENUM (
                        'Married', 'Widowed',
                        'Separated', 'Divorced',
                        'Single');
                        
                        CREATE TYPE bloods AS ENUM (
                        'A+', 'A-',
                        'B+', 'B-',
                        'AB+', 'AB-',
                        'O+', 'O-');
                        
                        CREATE TYPE orientation AS ENUM (
                        'Lesbian', 'Gay', 'Bisexual', 'Pansexual',
                        'Asexual','Non-binary', 'Straight');
                        
                        CREATE countries AS ENUM (
                        'Angola', 'Argentina', 'Armenia', 'Australia',
                        'Bahamas', 'Bangladesh', 'Bolivia', 'Brazil',
                        'Canada', 'Chile', 'China', 'Ecuador',
                        'Egypt', 'Finland', 'France', 'Germany',
                        'Greece', 'Guinea', 'Hungary' 'India',
                        'Indonesia', 'Italy', 'Jamaica', 'Japan',
                        'Malaysia', 'Maldives', 'Mexico', 'Monaco',
                        'Morocco', 'Netherlands', 'New Zealand', 'Nigeria',
                        'Paraguay', 'Peru', 'Philippines', 'Poland',
                        'Portugal', 'Romania', 'Russian Federation', 'Senegal',
                        'Singapore', 'Slovakia', 'Slovenia', 'Somalia',
                        'Spain', 'Sweden', 'Switzerland', 'Taiwan',
                        'Thailand', 'Ukraine', 'United Kingdom', 'United States',
                        'Uruguay');

                        CREATE TABLE IF NOT EXISTS mage (
                        id              uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
                        name            varchar(56) NOT NULL,
                        gender          genders NOT NULL,
                        sexuality       orientation NOT NULL,
                        country         countries NOT NULL,
                        age             int NOT NULL,
                        job             varchar(32) NOT NULL,
                        blood           bloods NOT NULL,
                        relationship    martial NOT NULL,
                        tradition       traditions NOT NULL,
                        character       playable NOT NULL,
                        creator         varchar(56) NOT NULL,
                        );
                        
'''
sql.execute(create_table)

sql.close()
database.close()
