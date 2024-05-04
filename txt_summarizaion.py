from summarizer import Summarizer
import warnings

def summarizing(text):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=FutureWarning)
        summarizer = Summarizer()

    summary = summarizer(text)

    return summary




#print(summarizing("بالطبيعة تتجلى عظمة الخالق وروعة الحياة، فهي لوحة فنية تتألق بألوانها المتنوعة وتنوع مظاهرها. في عمق الغابات تتراقص أوراق الأشجار بلطف مع نسمات الهواء، وتتغنى الطيور بألحانها الجميلة، معزوفة طبيعية تعزفها الحياة بكل أناقة. تتدفق الأنهار بسلاسة، تروي أرضا جدباء وتمنح الحياة لكل ما يمسها، وتنحت الجبال بعظمتها وجمالها، تحمل عبق التاريخ وقصص الأجيال. تنتشر الزهور في كل مكان، تعطي لمسة من البهجة والحيوية، وترسم الألوان المختلفة لوحة فاتنة على وجه الأرض. تعتبر الطبيعة ملاذًا للروح، تمنح الهدوء والسكينة، وتجدد الحياة بكل ما فيها. ففي أحضانها، يجد الإنسان الراحة والاسترخاء، ويستعيد توازنه الداخلي. لذلك، فإن الحفاظ على الطبيعة ومواردها يعد من واجباتنا تجاه هذه الكنوز الثمينة التي وهبها الله لنا."))