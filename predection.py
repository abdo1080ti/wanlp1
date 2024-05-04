
import joblib
from sentiment_analysis import sent_analysis

my_model= joblib.load('new_press_articles_classifier.pkl')
count_vectorizer= joblib.load('count_vctorizer.pkl')
tfidf_vectorizer= joblib.load('tfidf_vctorizer.pkl')
def categories_category(category):
    if category == 1:
        return 'Sports'
    elif category == 2:
        return 'Politics'
    elif category == 3:
        return 'Culture'
    elif category == 4:
        return 'Finance'
    elif category == 5:
        return 'Medical'
    elif category == 6:
        return 'Religion'
    elif category == 7:
        return 'Tech'
    elif category == 8:
        return 'Cars'
    elif category == 9:
        return 'Economy'
    elif category == 10:
        return 'Health'
    elif category == 11:
        return 'Tourism'
categories = []
def predect_new_category(article):

    #sentiment = sent_analysis(article)
    #summary = summarizing(article)
    tokens = article[0].split()
    num_tokens = len(tokens)
    part_size = num_tokens // 5
    the_last_one = num_tokens % 5

    parts = [tokens[i * part_size:(i + 1) * part_size] for i in range(5)]
    if the_last_one:
        parts[-1].extend(tokens[-the_last_one:])

    part1, part2, part3, part4, part5 = parts
    subarticle1 = " ".join(part1)
    subarticle2 = " ".join(part2)


    article_tfidf_vctorizer1 = tfidf_vectorizer.transform(part1)
    article_tfidf_vctorizer2 = tfidf_vectorizer.transform(part2)
    article_tfidf_vctorizer3 = tfidf_vectorizer.transform(part3)
    article_tfidf_vctorizer4 = tfidf_vectorizer.transform(part4)
    article_tfidf_vctorizer5 = tfidf_vectorizer.transform(part5)

    categor1 = categories_category(my_model.predict(article_tfidf_vctorizer1)[0])
    categor2 = categories_category(my_model.predict(article_tfidf_vctorizer2)[0])
    categor3 = categories_category(my_model.predict(article_tfidf_vctorizer3)[0])
    categor4 = categories_category(my_model.predict(article_tfidf_vctorizer4)[0])
    categor5 = categories_category(my_model.predict(article_tfidf_vctorizer5)[0])


    probabilities1 = my_model.predict_proba(article_tfidf_vctorizer1)
    p1_sport = probabilities1[0][0]
    p1_politics = probabilities1[0][1]
    p1_Culture = probabilities1[0][2]
    p1_Finance = probabilities1[0][3]
    p1_Medical = probabilities1[0][4]
    p1_Religion = probabilities1[0][5]
    p1_Tech = probabilities1[0][6]
    p1_Cars = probabilities1[0][7]
    p1_Economy = probabilities1[0][8]
    p1_Health= probabilities1[0][9]
    p1_Tourism = probabilities1[0][10]

    probabilities2 = my_model.predict_proba(article_tfidf_vctorizer2)
    p2_sport = probabilities2[0][0]
    p2_politics = probabilities2[0][1]
    p2_Culture = probabilities2[0][2]
    p2_Finance = probabilities2[0][3]
    p2_Medical = probabilities2[0][4]
    p2_Religion = probabilities2[0][5]
    p2_Tech = probabilities2[0][6]
    p2_Cars = probabilities2[0][7]
    p2_Economy = probabilities2[0][8]
    p2_Health= probabilities2[0][9]
    p2_Tourism = probabilities2[0][10]

    probabilities3 = my_model.predict_proba(article_tfidf_vctorizer3)
    p3_sport = probabilities3[0][0]
    p3_politics = probabilities3[0][1]
    p3_Culture = probabilities3[0][2]
    p3_Finance = probabilities3[0][3]
    p3_Medical = probabilities3[0][4]
    p3_Religion = probabilities3[0][5]
    p3_Tech = probabilities3[0][6]
    p3_Cars = probabilities3[0][7]
    p3_Economy = probabilities3[0][8]
    p3_Health= probabilities3[0][9]
    p3_Tourism = probabilities3[0][10]

    probabilities4 = my_model.predict_proba(article_tfidf_vctorizer4)
    p4_sport = probabilities4[0][0]
    p4_politics = probabilities4[0][1]
    p4_Culture = probabilities4[0][2]
    p4_Finance = probabilities4[0][3]
    p4_Medical = probabilities4[0][4]
    p4_Religion = probabilities4[0][5]
    p4_Tech = probabilities4[0][6]
    p4_Cars = probabilities4[0][7]
    p4_Economy = probabilities4[0][8]
    p4_Health= probabilities4[0][9]
    p4_Tourism = probabilities4[0][10]

    probabilities5 = my_model.predict_proba(article_tfidf_vctorizer5)
    p5_sport = probabilities5[0][0]
    p5_politics = probabilities5[0][1]
    p5_Culture = probabilities5[0][2]
    p5_Finance = probabilities5[0][3]
    p5_Medical = probabilities5[0][4]
    p5_Religion = probabilities5[0][5]
    p5_Tech = probabilities5[0][6]
    p5_Cars = probabilities5[0][7]
    p5_Economy = probabilities5[0][8]
    p5_Health= probabilities5[0][9]
    p5_Tourism = probabilities5[0][10]

    pt_sport = ((p1_sport + p2_sport +p3_sport + p4_sport +p5_sport )*500) /11
    pt_politics = ((p1_politics + p2_politics +p3_politics + p4_politics +p5_politics)*500) /11
    pt_Culture = ((p1_Culture + p2_Culture +p3_Culture + p4_Culture +p5_Culture)*500) /11

    pt_Finance = ((p1_Finance + p2_Finance +p3_Finance + p4_Finance +p5_Finance ) *500) /11
    pt_medical = ((p1_Medical + p2_Medical +p3_Medical + p4_Medical +p5_Medical) *500) /11
    pt_Religion = ((p1_Religion + p2_Religion +p3_Religion + p4_Religion +p5_Religion)*500) /11

    pt_Tech = ((p1_Tech + p2_Tech +p3_Tech + p4_Tech +p5_Tech )*500) /11
    pt_Cars = ((p1_Cars + p2_Cars +p3_Cars + p4_Cars +p5_Cars) *500) /11
    pt_Economy = ((p1_Economy + p2_Economy +p3_Economy + p4_Economy +p5_Economy) *500) /11

    pt_Health = ((p1_Health + p2_Health +p3_Health + p4_Health +p5_Health ) *500) /11
    pt_Tourism = ((p1_Tourism + p2_Tourism +p3_Tourism + p4_Tourism +p5_Tourism) *500) /11

    ctegory_set = {categor1,categor2,categor3,categor4,categor5}

    category_probabilities = {
        'Sports': pt_sport,
        'Politics': pt_politics,
        'Culture': pt_Culture,
        'Finance': pt_Finance,
        'Medical': pt_medical,
        'Religion': pt_Religion,
        'Tech': pt_Tech,
        'Cars': pt_Cars,
        'Economy': pt_Economy,
        'Health': pt_Health,
        'Tourism': pt_Tourism
    }

    max_ctegory = max(category_probabilities, key=category_probabilities.get)
    
    other = 100
    all_category_probalities = []
    for category in ctegory_set:
        if category in category_probabilities:
            c = (category, category_probabilities[category])
            all_category_probalities.append(c)
            #print("Probability of", category, ":", category_probabilities[category])
            other -= category_probabilities[category]
        else:
            #print("Category", category, "not found in probabilities.")
            continue

    return ctegory_set, max_ctegory, all_category_probalities, other

article3 = [
    'كاسبرسكي تطلق برنامج لمكافحة الفيروسات للحواسب اللوحية بنظام أندرويد تقدم كاسبرسكي لاب المنتج الجديد Kaspersky Tablet Security المصمم خصيصا لحماية الحواسب اللوحية التي تعمل بنظام تشغيل Android.وقد راعى خبراء كاسبرسكي لاب جميع مواصفات الحواسب اللوحية وبالنتيجة طرحت حل أمني مخصص لها، يؤمن الحماية من البرمجيات الخبيثة والتطبيقات الاحتيالية من جهة، وحصانة للبيانات الشخصية في حال ضياع أو سرقة الجهاز من جهة أخرى.ويوفر Kaspersky Tablet Security حماية شاملة من جميع نشاطات المجرمين الالكترونيين، المطور تحديدا للحواسب اللوحية التي تعمل بـAndroid. ويعمل المحرك المكافح للفيروسات في هذا المنتج بالتشارك مع تقنية الحوسبة السحابية ليضمن تعطيل نشاط جميع البرمجيات الخبيثة الجديدة وغير المعروفة على حد سواء.يقدم Kaspersky Tablet Security أيضا خاصية Web Protection التي تساعد على تعطيل عمل المواقع الخبيثة أو الاحتيالية لدى استخدام متصفح Android.كما أنه يجنب المستخدم من دخول المواقع الضارة التي تهدف إلى سرقة بيانات التسجيل إلى مواقع التواصل الاجتماعي أو تلك المتعلقة بحسابه البنكي على الانترنت. كما يعمل Kaspersky Tablet Security عن بعد، إذا يمكنه أن يعطل عمل الجهاز الضائع أو المسروق وحتى حذف جميع البيانات الشخصية منه.بإمكان المنتج أن يحدد موقع الجهاز الضائع أو المسروق، ليس فقط بمساعدة GPS بل و شبكة GSM أو إحداثيات أقرب نقطة الاتصال بالشبكة اللاسلكية Wi-Fi.كما تساعد وظيفة Mugshot على التقاط الصور بشكل خفي للشخص الذي يستخدم الجهاز الذي سرق أو ضاع بواسطة كاميرا مدمجة وينقل الصور إلى صاحب الجهاز. وصممت الواجهة بشكل يلائم حواسب Android اللوحية، مراعية أوجه الشبه والاختلاف مع الهواتف الذكية والحواسب الشخصية.الخصائص الأساسية – مكافح الفيروسات: حماية من البرمجيات الخبيثة والتطبيقات الاحتيالية بالزمن الفعلي – حماية “سحابية”: تؤمن ردا سريعا على التهديدات الجديدة والناشئة – حماية الويب: يشخص ويعطل عناوين URL الخبيثة وصفحات الويب الخطيرة بما فيها المواقع التصيدية – Web Management: واجهة ويب للتحكم عن بعد بالجهاز – مكافح السرقة: حماية مُحكمة للبيانات في جميع الظروف • خاصية Find: إمكانية البحث عن الجهاز الضائع أو المسروق باستخدام نظامي GPS، GSM أو Wi-Fi • تعطيل الجهاز وحذف البيانات: إمكانية تعطيل عمل الجهاز وحذف البيانات الشخصية منه • التقاط “الصور البوليسية”: إمكانية التقاط الصور خفيةً من الجهاز وإرسالها إلى صاحبهو في ديسمبر 2011 ، تجاوزت حالات استهداف البرمجيات الخبيثة للأجهزة المحمولة 6400 حالة وفقا لمعطيات كاسبرسكي لاب. وارتفع عدد التطبيقات الخبيثة المصممة لمنصة Android إلى 65 بالمائة من إجمالي التطبيقات الخبيثة للأجهزة المحمولة، وروجت حتى عبر المتجر الالكتروني الرسمي Android Market. والأكثر من ذلك أن البرمجيات الخبيثة التي تستهدف هذه المنصة هي الأكثر تعقيدا من بين جميع البرمجيات الخبيثة.هذا ويتطور سوق الحواسب اللوحية بسرعة، حيث جاء في توقعات نشرها محللو Gartner أنه في عام 2015 سيباع أكثر من 300 مليون حاسب لوحي وستتزايد حصة سوق Android باستمرار.وبحكم نمو شعبية الحواسب اللوحية من الواضح أن عدد الهجمات على هذه الاجهزة ستزداد أيضا، وسيكون الهدف الرئيسي للمجرمين الالكترونيين هو سرقة البيانات الشخصية للمستخدمين.'
]

ctegory_set, max_ctegory, all_category_probalities, other = predect_new_category(article3)

print(f'this article is of {ctegory_set} where majority of it is {max_ctegory}')

print("the probabilities are as follow:")

for i in all_category_probalities:
    print(f'Probability of {i[0]} : {i[1]} ')
print(f'and the other is: {other}')

#print(predect_new_category(article3))