# prompt_for_low_your_period_pain='''You have to act as a gynecologist doctor and you have to provide some advise or exorcise based on my symptoms that reduce my period pain 
#  there are some key factors like the advice must be this format

# 1.advice no 1
# 2.advice no 2
# 3.advice no 3


# here is my symptoms '''


prompt_for_low_your_period_pain='''You are a gynecologist. Based on the following symptoms, provide advice or exercises to reduce period pain.
Ensure the advice is numbered and follows this structure:

Advice no 1
Advice no 2
Advice no 3
Advice no 4

here is my symptoms

'''


prompt_for_pragnency_traker='''You are a doctor providing important health tips to a pregnant woman. Based on the month of her pregnancy, give tailored advice that addresses her specific needs.
The tips should focus on maintaining a healthy lifestyle, addressing common symptoms, and preparing for the upcoming stages of pregnancy.

Some example tips could include:

1.Stay Hydrated: Encourage drinking plenty of water throughout the day to prevent dehydration, which can cause fatigue and increase the risk of preterm labor.

2.Balanced Nutrition: Recommend a well-balanced diet that includes fruits, vegetables, whole grains, and lean proteins. Emphasize the importance of getting extra nutrients as the baby grows.

3.Rest and Sleep: Advise on how to rest comfortably. Suggest lying on her side with pillows to support the belly and legs, which can help alleviate discomfort during sleep.

4.Frequent Walks: Gentle walking can enhance circulation and may help position the baby optimally for labor.

5.Please provide month-specific advice considering the particular needs, changes, and symptoms associated with each stage of pregnancy.

month:{month}
'''


prompt_for_fashion_with_photo='''Analyze the skin color and tone of individuals in the provided image. Based on each skin tone,  
recommend suitable outfit colors and styles that complement or enhance the complexion. 
Describe each outfit choice in detail, including color, fabric, and style preferences based on the identified skin tone'''


prompt_for_hair_care = '''
Provide a comprehensive hair care guide tailored to the user's specific hair type and current weather conditions. Include detailed tips on maintaining healthy hair, addressing any potential issues, and recommending foods that support hair health. Ensure that the guidance is practical, seasonally appropriate, and considers hair type and environmental factors.

- Hair Type: {hair_type}
- Weather: {weather}
  
Please cover:
1. Daily hair care routine and best practices for this hair type.
2. Recommended products or natural ingredients suited to this hair type and weather.
3. Nutritional suggestions (foods, vitamins, etc.) that promote hair health for this hair type and weather.
4. Precautions to protect hair from weather-related challenges.
'''

prompt_for_skin_care_tips='''Analyze the provided image to accurately identify the predominant skin tone of the individuals present.

Question:
{question}

Skin Type:
{skin}

Response Guidelines:

1.Provide a comprehensive response that addresses the specific question.
2.Consider the identified skin tone when suggesting products, treatments, or advice.
3.Offer personalized recommendations based on the skin type provided.
4.Use clear and concise language, avoiding technical jargon.
5.If the image quality is insufficient for accurate skin tone identification, state so explicitly.
'''

prompt_for_occasion_wise_outfit='''Examine the skin tone in the provided image and create an outfit and accessory recommendation tailored for the specified event. 
Suggest attire, including tops, bottoms, skirts, dresses, and shoes, that harmonizes beautifully with her skin tone and reflects current fashion trends. Include accessories that enhance her look,
ensuring each piece complements her unique style for a cohesive, chic outfit perfect for the event.
event:{event}

'''

prompt_for_pimple_remove=''' Analyze the skin condition visible in the provided image and provide practical, over-the-counter 
recommendations for reducing pimples. 
 Please include:
 1. A detailed skincare routine with specific product types for morning and evening (e.g., gentle 
cleansers, acne treatments, moisturizers, sunscreen) tailored to acne-prone skin.
 2. Suggested active ingredients (like salicylic acid, benzoyl peroxide, niacinamide) that can help 
reduce pimples and inflammation.
 3. Lifestyle and dietary suggestions, such as foods to avoid or consume, and habits that can 
promote clearer skin.
 Avoid suggesting consulting a dermatologist, and instead focus on practical steps that the user can 
try independently.
 Offer advice specific to the visible skin condition in the image without mentioning the need for 
medical consultation.'''


prompt_for_glow_skin='''Analyze the skin condition visible in the provided image and provide practical, over-the-counter 
recommendations for achieving a natural glow. 
 Please include:
 1. A detailed skincare routine with specific product types for morning and evening (e.g., gentle 
cleansers, hydrating serums, moisturizers, sunscreen) tailored to enhance skin radiance.
 2. Suggested active ingredients (like vitamin C, hyaluronic acid, niacinamide) that can improve skin 
texture, hydration, and brightness.
 3. Lifestyle and dietary suggestions, such as foods that promote healthy skin and habits that can 
enhance a natural glow.
 Focus on practical steps the user can try independently, specific to the visible skin condition in the 
image, without mentioning the need for medical consultation.'''



prompt_for_cycle_traker='''Given the user's last period start date in the format dd/mm/yyyy as $selectedDate, calculate the 
next period date by adding 28 days to the input date. Make sure to correctly adjust for changes in the 
day, month, and year as needed to provide an accurate prediction. Return the next period date in the 
same dd/mm/yyyy format and include tips for managing common menstrual symptoms.

date={date}'''


prompt_for_Exercise_diet='''Based on my height(feet), weight(kg), age(years), and gender of female, 
 create a personalized one-month diet plan. The plan should consider my aiming to support my 
specific needs (e.g., weight loss, weight gain, maintenance, 
 or overall health improvement). 
 The plan should include 3 main meals (Breakfast, Lunch, Dinner) and 2 snacks per day. Each meal 
should have:
 - A brief description of the food and its nutritional purpose.
 - The exact time the meal should be eaten.
 - Any specific dietary considerations (e.g., vegetarian, gluten-free).
 Format the response as follows:
 Breakfast: [meal description, dietary considerations if any] at [time]
 Lunch: [meal description, dietary considerations if any] at [time]
 Dinner: [meal description, dietary considerations if any] at [time]
 Snack 1: [meal description, dietary considerations if any] at [time]
 Snack 2: [meal description, dietary considerations if any] at [time]
 height:{height}
 weight:{weight}
 age:{age}
 
 '''

prompt_for_Exercise_fitness='''
Based on my height of $height (feet), weight of $weight kg, age of $age years, and gender female, 
 create a personalized one-month exercise plan. 
 The plan should include daily exercises split into morning and evening sessions. Each exercise 
should specify the type of exercise, duration, intensity, and target muscle groups or fitness goals 
(e.g., cardio, strength, flexibility, balance).
 Format the response as follows:
 Day 1:
 - Morning Exercise: [exercise description] for [duration] at [intensity level] (target areas)
 - Evening Exercise: [exercise description] for [duration] at [intensity level] (target areas)
 Please ensure the exercises vary throughout the month to cover different aspects of fitness, such 
as cardio, strength training, flexibility, and balance, and are suitable for my profile.

height:{height}
 weight:{weight}
 age:{age}
 

'''