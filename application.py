#IMPORTING OF REQUIRED LIBRARIES
from flask import Flask, jsonify, json, request
import pandas as pd
import numpy as np
import DateTime
from datetime import date


#CREATING FLASK APPLICATION AND REQUIRED URL
application=Flask(__name__)

@application.route('/api/v1.0/yearly_sales/', methods=['GET'])
def get_yearly_sales():

    store_code_present = True
    if 'store_code' in request.args:
        store_code = int(request.args['store_code'])

    else:
        store_code_present = False

    state_present = True
    if 'state' in request.args:
        state = (request.args['state'])

    else:
        state_present = False

    age_group_present = True
    if 'age_group' in request.args:
        age_group = (request.args['age_group'])

    else:
        age_group_present = False

    gender_present = True
    if 'gender' in request.args:
        gender = (request.args['gender'])

    else:
        gender_present = False


#IMPORT RETAIL DATA FILE (excel)

    bbazar = pd.read_excel(r"C:\Users\murali\Documents\my project\bigbazar_dataset.xlsx")
    bbazar['year'] = pd.DatetimeIndex(bbazar['transactionDate']).year

    if store_code_present == True:
        sbazar = bbazar[(bbazar['store_code'] == store_code)]
        year_counts = (sbazar['store_code'].value_counts()).to_dict()
        total_sales = ((sbazar[['store_code', 'sale_price_after_promo']]).groupby('store_code').sum()).to_dict()
        return jsonify(year_counts, total_sales)

    if state_present == True:
        stbazar = bbazar[(bbazar['State'] == state)]
        year_counts = (stbazar['State'].value_counts()).to_dict()
        total_sales = ((stbazar[['State', 'sale_price_after_promo']]).groupby('State').sum()).to_dict()
        return jsonify(year_counts, total_sales)

    if age_group_present == True:
        bbazar['DOB'] = pd.to_datetime(bbazar['DOB'], errors='coerce')
        bbazar['year_of_birth'] = pd.DatetimeIndex(bbazar['DOB']).year
        bbazar['age'] = date.today().year - bbazar['year_of_birth']
        bins = [0, 30, 45, 65, 107]
        group_names = ['a1', 'a2', 'a3', 'a4']
        bbazar['age_group'] = pd.cut(np.array(bbazar['age']), bins, labels=group_names)
        sgbazar = bbazar[(bbazar['age_group'] == age_group)]
        year_counts = (sgbazar['age_group'].value_counts()).sort_index().to_dict()
        total_sales = sgbazar[['age_group', 'sale_price_after_promo']].groupby('age_group').sum().to_dict()
        return jsonify(year_counts, total_sales)



    if gender_present == True:
        gbazar = bbazar[(bbazar['Gender'] == gender)]
        year_counts = (gbazar['Gender'].value_counts()).to_dict()
        total_sales = ((gbazar[['Gender', 'sale_price_after_promo']]).groupby('Gender').sum()).to_dict()
        return jsonify(year_counts, total_sales)


    year_counts = (bbazar['year'].value_counts().sort_index()).to_dict()
    total_sales = ((bbazar[['year', 'sale_price_after_promo']]).groupby('year').sum()).to_dict()
    return jsonify(year_counts, total_sales)


@application.route('/api/v1.0/quarterly_sales/', methods=['GET'])
def get_quarterly_sales():

    year_present = True
    if 'year' in request.args:
        year = int(request.args['year'])

    else:
        year_present = False

    store_code_present = True
    if 'store_code' in request.args:
        store_code = int(request.args['store_code'])

    else:
        store_code_present = False

    state_present = True
    if 'state' in request.args:
        state = (request.args['state'])

    else:
        state_present = False

    age_group_present = True
    if 'age_group' in request.args:
        age_group = (request.args['age_group'])

    else:
        age_group_present = False

    gender_present = True
    if 'gender' in request.args:
        gender = (request.args['gender'])

    else:
        gender_present = False



    bbazar = pd.read_excel(r"C:\Users\murali\Documents\my project\bigbazar_dataset.xlsx")
    bbazar['year'] = pd.DatetimeIndex(bbazar['transactionDate']).year
    bbazar2 = bbazar[(bbazar['year'] == year)]
    bbazar2['quarter'] = pd.DatetimeIndex(bbazar2['transactionDate']).quarter

    if store_code_present == True:
        sbazar = bbazar2[(bbazar2['store_code'] == store_code)]
        year_counts = (sbazar[['quarter']].groupby('quarter')).size().to_dict()
        total_sales = (sbazar[['quarter', 'sale_price_after_promo']]).groupby('quarter').sum().to_dict()
        return jsonify( year_counts,total_sales)

    if state_present == True:

        stbazar = bbazar2[(bbazar2['State'] == state)]
        year_counts = (stbazar[['quarter']].groupby('quarter')).size().to_dict()
        total_sales = (stbazar[['quarter', 'sale_price_after_promo']]).groupby('quarter').sum().to_dict()
        return jsonify(year_counts, total_sales)

    if age_group_present == True:
        bbazar2['DOB'] = pd.to_datetime(bbazar2['DOB'], errors='coerce')
        bbazar2['year_of_birth'] = pd.DatetimeIndex(bbazar2['DOB']).year
        bbazar2['age'] = bbazar2['year'] - bbazar2['year_of_birth']
        bins = [0, 30, 45, 65, 107]
        group_names = ['a1', 'a2', 'a3', 'a4']
        bbazar2['age_group'] = pd.cut(np.array(bbazar2['age']), bins, labels=group_names)
        sgbazar = bbazar2[(bbazar2['age_group'] == age_group)]
        year_counts = (sgbazar[['quarter']].groupby('quarter')).size().to_dict()
        total_sales = (sgbazar[['quarter', 'sale_price_after_promo']]).groupby('quarter').sum().to_dict()
        return jsonify(year_counts, total_sales)

    if gender_present == True:
        gbazar = bbazar2[(bbazar2['Gender'] == gender)]
        year_counts = (gbazar['quarter'].value_counts()).to_dict()
        total_sales = ((gbazar[['quarter', 'sale_price_after_promo']]).groupby('quarter').sum()).to_dict()
        return jsonify(year_counts, total_sales)




    year_counts = ((bbazar2[['quarter']].groupby('quarter')).size()).to_dict()
    total_sales = ((bbazar2[['quarter', 'sale_price_after_promo']]).groupby('quarter').sum()).to_dict()
    return jsonify(year_counts, total_sales)

@application.route('/api/v1.0/monthly_sales/', methods=['GET'])
def get_monthly_sales():

    year_present = True
    if 'year' in request.args:
        year = int(request.args['year'])

    else:
        year_present = False

    store_code_present = True
    if 'store_code' in request.args:
        store_code = int(request.args['store_code'])

    else:
        store_code_present = False

    state_present = True
    if 'state' in request.args:
        state = (request.args['state'])

    else:
        state_present = False

    age_group_present = True
    if 'age_group' in request.args:
        age_group = (request.args['age_group'])

    else:
        age_group_present = False

    gender_present = True
    if 'gender' in request.args:
        gender = (request.args['gender'])

    else:
        gender_present = False

    bbazar = pd.read_excel(r"C:\Users\murali\Documents\my project\bigbazar_dataset.xlsx")
    bbazar['year'] = pd.DatetimeIndex(bbazar['transactionDate']).year
    bbazar2 = bbazar[(bbazar['year'] == year)]
    bbazar2['month'] = pd.DatetimeIndex(bbazar2['transactionDate']).month

    if store_code_present == True:
        sbazar = bbazar2[(bbazar2['store_code'] == store_code)]
        year_counts = (sbazar[['month']].groupby('month')).size().to_dict()
        total_sales = (sbazar[['month', 'sale_price_after_promo']]).groupby('month').sum().to_dict()
        return jsonify(year_counts, total_sales)

    if state_present == True:
        stbazar = bbazar2[(bbazar2['State'] == state)]
        year_counts = (stbazar[['month']].groupby('month')).size().to_dict()
        total_sales = (stbazar[['month', 'sale_price_after_promo']]).groupby('month').sum().to_dict()
        return jsonify(year_counts, total_sales)

    if age_group_present == True:
        bbazar2['DOB'] = pd.to_datetime(bbazar2['DOB'], errors='coerce')
        bbazar2['year_of_birth'] = pd.DatetimeIndex(bbazar2['DOB']).year
        bbazar2['age'] = bbazar2['year'] - bbazar2['year_of_birth']
        bins = [0, 30, 45, 65, 107]
        group_names = ['a1', 'a2', 'a3', 'a4']
        bbazar2['age_group'] = pd.cut(np.array(bbazar2['age']), bins, labels=group_names)
        sgbazar = bbazar2[(bbazar2['age_group'] == age_group)]
        year_counts = (sgbazar[['month']].groupby('month')).size().to_dict()
        total_sales = (sgbazar[['month', 'sale_price_after_promo']]).groupby('month').sum().to_dict()
        return jsonify(year_counts, total_sales)

    if gender_present == True:
        gbazar = bbazar2[(bbazar2['Gender'] == gender)]
        year_counts = (gbazar['month'].value_counts()).to_dict()
        total_sales = ((gbazar[['month', 'sale_price_after_promo']]).groupby('month').sum()).to_dict()
        return jsonify(year_counts, total_sales)

    year_counts = ((bbazar2[['month']].groupby('month')).size()).to_dict()
    total_sales = ((bbazar2[['month', 'sale_price_after_promo']]).groupby('month').sum()).to_dict()
    return jsonify(year_counts, total_sales)

@application.route('/api/v1.0/daily_sales/', methods=['GET'])
def get_daily_sales():

    year_present = True
    if 'year' in request.args:
        year = int(request.args['year'])

    else:
        year_present = False

    month_present = True
    if 'month' in request.args:
        month = int(request.args['month'])

    else:
        month_present = False

    store_code_present = True
    if 'store_code' in request.args:
        store_code = int(request.args['store_code'])

    else:
        store_code_present = False

    state_present = True
    if 'state' in request.args:
        state = (request.args['state'])

    else:
        state_present = False

    bbazar = pd.read_excel(r"C:\Users\murali\Documents\my project\bigbazar_dataset.xlsx")
    bbazar['year'] = pd.DatetimeIndex(bbazar['transactionDate']).year
    bbazar2 = bbazar[(bbazar['year'] == year)]
    bbazar2['month'] = pd.DatetimeIndex(bbazar2['transactionDate']).month
    bbazar3 = bbazar2[(bbazar2['month'] == month)]
    bbazar3['day'] = pd.DatetimeIndex(bbazar3['transactionDate']).day

    if store_code_present == True:
        sbazar = bbazar3[(bbazar3['store_code'] == store_code)]
        year_counts = (sbazar[['day']].groupby('day')).size().to_dict()
        total_sales = (sbazar[['day', 'sale_price_after_promo']]).groupby('day').sum().to_dict()
        return jsonify(year_counts, total_sales)

    if state_present == True:
        stbazar = bbazar3[(bbazar3['State'] == state)]
        year_counts = (stbazar[['day']].groupby('day')).size().to_dict()
        total_sales = (stbazar[['day', 'sale_price_after_promo']]).groupby('day').sum().to_dict()
        return jsonify(year_counts, total_sales)


    year_counts = (bbazar3['day'].value_counts().sort_index()).to_dict()
    total_sales = ((bbazar3[['day', 'sale_price_after_promo']]).groupby('day').sum()).to_dict()
    return jsonify(year_counts, total_sales)

@application.route('/api/v1.0/weekday_sales/', methods=['GET'])
def get_weekday_sales():
    year_present = True
    if 'year' in request.args:
        year = int(request.args['year'])

    else:
        year_present = False

    month_present = True
    if 'month' in request.args:
        month = int(request.args['month'])

    else:
        month_present = False

    store_code_present = True
    if 'store_code' in request.args:
        store_code = int(request.args['store_code'])

    else:
        store_code_present = False

    state_present = True
    if 'state' in request.args:
        state = (request.args['state'])

    else:
        state_present = False

    bbazar = pd.read_excel(r"C:\Users\murali\Documents\my project\bigbazar_dataset.xlsx")
    bbazar['year'] = pd.DatetimeIndex(bbazar['transactionDate']).year
    bbazar2 = bbazar[(bbazar['year'] == year)]
    bbazar2['weekday'] = pd.DatetimeIndex(bbazar2['transactionDate']).day_name()

    if store_code_present == True:
        sbazar = bbazar2[(bbazar2['store_code'] == store_code)]
        year_counts = (sbazar[['weekday']].groupby('weekday')).size().to_dict()
        total_sales = (sbazar[['weekday', 'sale_price_after_promo']]).groupby('weekday').sum().to_dict()
        return jsonify(year_counts, total_sales)

    if state_present == True:
        stbazar = bbazar2[(bbazar2['State'] == state)]
        year_counts = (stbazar[['weekday']].groupby('weekday')).size().to_dict()
        total_sales = (stbazar[['weekday', 'sale_price_after_promo']]).groupby('weekday').sum().to_dict()
        return jsonify(year_counts, total_sales)

    year_counts = (bbazar2['weekday'].value_counts().sort_index()).to_dict()
    total_sales = ((bbazar2[['weekday', 'sale_price_after_promo']]).groupby('weekday').sum()).to_dict()
    return jsonify(year_counts, total_sales)

@application.route('/api/v1.0/promo_and_nonpromo_sales/', methods=['GET'])
def get_promo_and_nonpromo_sales():

    year_present = True
    if 'year' in request.args:
        year = int(request.args['year'])

    else:
        year_present = False

    bbazar = pd.read_excel(r"C:\Users\murali\Documents\my project\bigbazar_dataset.xlsx")
    bbazar['year'] = pd.DatetimeIndex(bbazar['transactionDate']).year
    bbazar2 = bbazar[(bbazar['year'] == year)]
    bbazar2['promo_code'] = np.where(bbazar2.promo_code != 'NONPROMO', 'PROMO', bbazar2.promo_code)
    year_counts = (bbazar2['promo_code'].value_counts().sort_index()).to_dict()
    total_sales = ((bbazar2[['promo_code', 'sale_price_after_promo']]).groupby('promo_code').sum()).to_dict()
    return jsonify(year_counts, total_sales)

@application.route('/api/v1.0/top_and_bottom_sales/', methods=['GET'])

def get_top_and_low_sales():
    year_present = True
    if 'year' in request.args:
        year = int(request.args['year'])

    else:
        year_present = False

    quarter_present = True
    if 'quarter' in request.args:
        quarter = int(request.args['quarter'])

    else:
        quarter_present = False

    month_present = True
    if 'month' in request.args:
        month = int(request.args['month'])

    else:
        month_present = False

    if 'chart_type' in request.args:
        chart_type = request.args['chart_type']

    else:
        return "chart type is missing"

    bbazar = pd.read_excel(r"C:\Users\murali\Documents\my project\bigbazar_dataset.xlsx")
    bbazar['year'] = pd.DatetimeIndex(bbazar['transactionDate']).year
    bbazar2 = bbazar[(bbazar['year'] == year)]
    bbazar2['quarter'] = pd.DatetimeIndex(bbazar2['transactionDate']).quarter
    bbazar2['month']=pd.DatetimeIndex(bbazar2['transactionDate']).month

    if chart_type == 'product_sales':
        if month_present == True:
            bbazarm = bbazar2[(bbazar2['month'] == month)]
            top_selling = bbazarm['product_code'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazarm['product_code'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

        if quarter_present == True:

            bbazarq = bbazar2[(bbazar2['quarter'] == quarter)]
            top_selling = bbazarq['product_code'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazarq['product_code'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

        if year_present == True:
            top_selling = bbazar2['product_code'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazar2['product_code'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

    if chart_type == 'state_sales':
        if month_present == True:
            bbazarm = bbazar2[(bbazar2['month'] == month)]
            top_selling = bbazarm['State'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazarm['State'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

        if quarter_present == True:
            bbazarq = bbazar2[(bbazar2['quarter'] == quarter)]
            top_selling = bbazarq['State'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazarq['State'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

        if year_present == True:
            top_selling = bbazar2['State'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazar2['State'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

    if chart_type == 'store_sales':

        if month_present == True:
            bbazarm = bbazar2[(bbazar2['month'] == month)]
            top_selling = bbazarm['store_code'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazarm['store_code'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

        if quarter_present == True:
            bbazarq = bbazar2[(bbazar2['quarter'] == quarter)]
            top_selling = bbazarq['store_code'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazarq['store_code'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)

        if year_present == True:
            top_selling = bbazar2['store_code'].value_counts(ascending=False).head(10).to_dict()
            low_selling = bbazar2['store_code'].value_counts(ascending=True).head(10).to_dict()
            return jsonify(top_selling, low_selling)





if __name__ == '__main__':
    application.run(debug=True)






