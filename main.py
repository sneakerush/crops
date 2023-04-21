from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    dropdown_options = ['Spring', 'Summer', 'Fall', 'Winter']
    return render_template('home.html', options=dropdown_options)

@app.route('/<season>')
def season(season):
    if season == 'spring':
        # Spring data here
        data = [    
            {'Crop': 'Asparagus', 'Days for Germination': '14', 'Harvest': '1095'},    
            {'Crop': 'Beets', 'Days for Germination': '5-10', 'Harvest': '45-60'},    
            {'Crop': 'Broccoli', 'Days for Germination': '5-10', 'Harvest': '55-100'},    
            {'Crop': 'Brussels Sprouts', 'Days for Germination': '5-10', 'Harvest': '80-115'},    
            {'Crop': 'Cabbage', 'Days for Germination': '5-10', 'Harvest': '50-100'},    
            {'Crop': 'Carrots', 'Days for Germination': '10-14', 'Harvest': '60-80'},    
            {'Crop': 'Cauliflower', 'Days for Germination': '5-10', 'Harvest': '55-100'},    
            {'Crop': 'Celery', 'Days for Germination': '10-14', 'Harvest': '85-120'},    
            {'Crop': 'Chard', 'Days for Germination': '7-14', 'Harvest': '50-60'},    
            {'Crop': 'Collard Greens', 'Days for Germination': '5-10', 'Harvest': '60-80'},    
            {'Crop': 'Endive', 'Days for Germination': '7-10', 'Harvest': '80-90'},    
            {'Crop': 'Kale', 'Days for Germination': '5-10', 'Harvest': '50-65 '},    
            {'Crop': 'Kohlrabi', 'Days for Germination': '5-10', 'Harvest': '50-60'},    
            {'Crop': 'Leeks', 'Days for Germination': '7-14', 'Harvest': '100-120'},    
            {'Crop': 'Lettuce', 'Days for Germination': '7-10', 'Harvest': '50-75'},    
            {'Crop': 'Mustard Greens', 'Days for Germination': '3-10', 'Harvest': '30-60'},    
            {'Crop': 'Onions', 'Days for Germination': '7-14', 'Harvest': '90-110'},    
            {'Crop': 'Parsley', 'Days for Germination': '14-21', 'Harvest': '70-90'},    
            {'Crop': 'Peas', 'Days for Germination': '7-14', 'Harvest': '50-70'},    
            {'Crop': 'Potatoes', 'Days for Germination': '14', 'Harvest': '75-135'},    
            {'Crop': 'Radishes', 'Days for Germination': '3-10', 'Harvest': '25-30'},    
            {'Crop': 'Rhubarb', 'Days for Germination': '14', 'Harvest': '730'},    
            {'Crop': 'Spinach', 'Days for Germination': '7-14', 'Harvest': '30-50'},    
            {'Crop': 'Swiss Chard', 'Days for Germination': '7-14', 'Harvest': '50-60'},    
            {'Crop': 'Turnips', 'Days for Germination': '3-10', 'Harvest': '35-75'}   
        ]
        return render_template('spring.html', data=data)

    elif season == 'summer':
        # Summer data here
        data = [
            {'Crop': 'Tomatoes', 'Days for Germination': '7', 'Harvest': '75'},    
            {'Crop': 'Peppers', 'Days for Germination': '14', 'Harvest': '90'},    
            {'Crop': 'Cucumbers', 'Days for Germination': '7', 'Harvest': '55'},    
            {'Crop': 'Squash', 'Days for Germination': '7', 'Harvest': '50'},    
            {'Crop': 'Zucchini', 'Days for Germination': '7', 'Harvest': '50'},    
            {'Crop': 'Corn', 'Days for Germination': '7', 'Harvest': '75'},    
            {'Crop': 'Green beans', 'Days for Germination': '7', 'Harvest': '50'},    
            {'Crop': 'Okra', 'Days for Germination': '7', 'Harvest': '50'},    
            {'Crop': 'Watermelon', 'Days for Germination': '7', 'Harvest': '100'},    
            {'Crop': 'Cantaloupe', 'Days for Germination': '7', 'Harvest': '100'},    
            {'Crop': 'Honeydew', 'Days for Germination': '7', 'Harvest': '100'},    
            {'Crop': 'Strawberries', 'Days for Germination': '14', 'Harvest': '180'},    
            {'Crop': 'Blueberries', 'Days for Germination': '30', 'Harvest': '180'},    
            {'Crop': 'Blackberries', 'Days for Germination': '14', 'Harvest': '180'},    
            {'Crop': 'Raspberries', 'Days for Germination': '30', 'Harvest': '180'},    
            {'Crop': 'Fig', 'Days for Germination': '14', 'Harvest': '365'},    
            {'Crop': 'Kiwi', 'Days for Germination': '30', 'Harvest': '1095'}
        ]

        return render_template('summer.html', data=data)

    elif season == 'fall':
        # Fall data here
        data = [    
            {'Crop': 'Arugula', 'Days for Germination': '3-7', 'Harvest': '20-45'},    
            {'Crop': 'Beets', 'Days for Germination': '7-14', 'Harvest': '50-70'},    
            {'Crop': 'Broccoli', 'Days for Germination': '5-10', 'Harvest': '60-100'},    
            {'Crop': 'Brussels Sprouts', 'Days for Germination': '5-10', 'Harvest': '90-180'},    
            {'Crop': 'Cabbage', 'Days for Germination': '5-10', 'Harvest': '60-100'},    
            {'Crop': 'Carrots', 'Days for Germination': '7-14', 'Harvest': '70-80'},    
            {'Crop': 'Cauliflower', 'Days for Germination': '5-10', 'Harvest': '60-100'},    
            {'Crop': 'Celery', 'Days for Germination': '14-21', 'Harvest': '90-120'},    
            {'Crop': 'Collard Greens', 'Days for Germination': '5-10', 'Harvest': '60-80'},    
            {'Crop': 'Endive', 'Days for Germination': '7-10', 'Harvest': '70-90'},    
            {'Crop': 'Garlic', 'Days for Germination': '14-21', 'Harvest': '240-300'},    
            {'Crop': 'Kale', 'Days for Germination': '5-10', 'Harvest': '60-80'},    
            {'Crop': 'Kohlrabi', 'Days for Germination': '5-10', 'Harvest': '40-60'},    
            {'Crop': 'Lettuce', 'Days for Germination': '7-14', 'Harvest': '30-70'},    
            {'Crop': 'Onions', 'Days for Germination': '7-14', 'Harvest': '100-175'},    
            {'Crop': 'Parsnips', 'Days for Germination': '14-21', 'Harvest': '120-180'},    
            {'Crop': 'Radishes', 'Days for Germination': '3-7', 'Harvest': '20-30'},    
            {'Crop': 'Spinach', 'Days for Germination': '7-14', 'Harvest': '40-50'},    
            {'Crop': 'Squash', 'Days for Germination': '7-10', 'Harvest': '50-60'},    
            {'Crop': 'Sweet Potatoes', 'Days for Germination': '14-21', 'Harvest': '100-150'},    
            {'Crop': 'Turnips', 'Days for Germination': '5-10', 'Harvest': '50-75'}
        ]

        return render_template('fall.html', data=data)

    elif season == 'winter':
        # Winter data here
        data = [
            {'Crop': 'Broccoli', 'Days for Germination': 5, 'Harvest': 70},
            {'Crop': 'Cabbage', 'Days for Germination': 7, 'Harvest': 80},
            {'Crop': 'Brussels Sprouts', 'Days for Germination': 10, 'Harvest': 90},
            {'Crop': 'Cauliflower', 'Days for Germination': 10, 'Harvest': 80},
            {'Crop': 'Spinach', 'Days for Germination': 7, 'Harvest': 45},
            {'Crop': 'Kale', 'Days for Germination': 5, 'Harvest': 55},
            {'Crop': 'Arugula', 'Days for Germination': 3, 'Harvest': 40},
            {'Crop': 'Lettuce', 'Days for Germination': 5, 'Harvest': 45},
            {'Crop': 'Radishes', 'Days for Germination': 3, 'Harvest': 25},
            {'Crop': 'Carrots', 'Days for Germination': 7, 'Harvest': 75},
            {'Crop': 'Beets', 'Days for Germination': 7, 'Harvest': 65},
            {'Crop': 'Turnips', 'Days for Germination': 5, 'Harvest': 50},
            {'Crop': 'Onions', 'Days for Germination': 7, 'Harvest': 100},
            {'Crop': 'Garlic', 'Days for Germination': 14, 'Harvest': 180},
            {'Crop': 'Peas', 'Days for Germination': 7, 'Harvest': 65},
            {'Crop': 'Broad Beans', 'Days for Germination': 7, 'Harvest': 80},
            {'Crop': 'Mache', 'Days for Germination': 5, 'Harvest': 40},
            {'Crop': 'Winter Purslane', 'Days for Germination': 5, 'Harvest': 30},
            {'Crop': 'Chard', 'Days for Germination': 7, 'Harvest': 70},
            {'Crop': 'Endive', 'Days for Germination': 7, 'Harvest': 70},
            {'Crop': 'Radicchio', 'Days for Germination': 10, 'Harvest': 85},
            {'Crop': 'Sorrel', 'Days for Germination': 7, 'Harvest': 60},
            {'Crop': 'Cress', 'Days for Germination': 3, 'Harvest': 20},
            {'Crop': 'Claytonia', 'Days for Germination': 5, 'Harvest': 40},
            {'Crop': 'Mustard Greens', 'Days for Germination': 5, 'Harvest': 45},
            {'Crop': 'Tatsoi', 'Days for Germination': 5, 'Harvest': 45},
            {'Crop': 'Komatsuna', 'Days for Germination': 5, 'Harvest': 45},
            {'Crop': 'Collard Greens', 'Days for Germination': 7, 'Harvest': 65},
            {'Crop': 'Mizuna', 'Days for Germination': 5, 'Harvest': 40},
            {'Crop': 'Scallions', 'Days for Germination': 7, 'Harvest': 90}
        ]

        return render_template('winter.html', data=data)
    else:
        # Handle invalid input here
        print(season)
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()