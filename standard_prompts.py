GENERATE_ESSAY_PROMPT_TEMPLATE = "Based on premise: \"{}\" generate story containing several scenes, use scene1:, scene2:, ... to represent."

RATE_ESSAY_PROMPT_TEMPLATE="Based on 1. Interesting. Interesting to the reader. 2. Coherent. Plot-coherent. 3. Relevant. Faithful to the initial premise. 4. Humanlike. Judged to be human-written.4 dimensions evaluate following 2 stories, the score is from 0 to 100, higher score means better.\nThe initial premise of story is \"{}\"\nStory 1: {}\n Story 2: {}."

SUMMEVAL_RATE_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Based on the following four categories: 1. Coherence (how well the summary is structured and organized).\n2. Consistency (the factual alignment between the summary and the summarized source).\n3. Fluency (the quality of individual sentences).\n4. Relevance (selection of important content from the source).\nEvaluate the following two summaries by assigning an integer score (from 1 to 5) to each category. Higher score means better.\n\nThe source to be summarized is:\n{}\n\nSummary1:\n{}\n\nSummary2:\n{}\n\nIn your response, please use the following format strictly and no need for any extra explanations: \n###Summary1 Ratings###\n**Coherence**: \n**Consistency**: \n**Fluency**: \n**Relevance**: \n\n###Summary2 Ratings###\n**Coherence**: \n**Consistency**: \n**Fluency**: \n**Relevance**: \n"

SUMMEVAL_RATE_EXPLAIN_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Based on the following four categories: 1. Coherence (how well the summary is structured and organized).\n2. Consistency (the factual alignment between the summary and the summarized source).\n3. Fluency (the quality of individual sentences).\n4. Relevance (selection of important content from the source).\nEvaluate the following two summaries by assigning an integer score (from 1 to 5) to each category. Higher score means better.\n\nThe source to be summarized is:\n{}\n\nSummary1:\n{}\n\nSummary2:\n{}\n\nIn your response, please use the following format strictly: \n###Summary1 Ratings###\n**Coherence**: \n**Consistency**: \n**Fluency**: \n**Relevance**: \n\n###Summary2 Ratings###\n**Coherence**: \n**Consistency**: \n**Fluency**: \n**Relevance**: \n\n###Explanations###:"

SUMMEVAL_ANALYZE_RATE_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Based on the following four categories: 1. Coherence (how well the summary is structured and organized).\n2. Consistency (the factual alignment between the summary and the summarized source).\n3. Fluency (the quality of individual sentences).\n4. Relevance (selection of important content from the source).\nEvaluate the following two summaries by first providing an analysis, and then assigning an integer score (from 1 to 5) to each category. Higher score means better.\n\nThe source to be summarized is:\n{}\n\nSummary1:\n{}\n\nSummary2:\n{}\n\nIn your response, please use the following format strictly:\n\n###Analysis###: \n###Summary1 Ratings###\n**Coherence**: \n**Consistency**: \n**Fluency**: \n**Relevance**: \n\n###Summary2 Ratings###\n**Coherence**: \n**Consistency**: \n**Fluency**: \n**Relevance**: \n"


MEVA_ANALYZE_RATE_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Evaluate the overall quality of the following two stories with respect to the given story prompt, by first providing an analysis, and then assigning an integer score (from 1 to 5) to each story. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format strictly:\n###Analysis###:\n\n###Story1 Ratings###\n**Overall Quality w.r.t. Prompt**: \n\n###Story2 Ratings###\n**Overall Quality w.r.t. Prompt**: \n"

MEVA_RATE_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Evaluate the overall quality of the following two stories with respect to the given story prompt, by assigning an integer score (from 1 to 5) to each story. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format strictly:\n###Story1 Ratings###\n**Overall Quality w.r.t. Prompt**: \n\n###Story2 Ratings###\n**Overall Quality w.r.t. Prompt**: \n"

MEVA_RATE_EXPLAIN_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Evaluate the overall quality of the following two stories with respect to the given story prompt, by assigning an integer score (from 1 to 5) to each story. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format strictly:\n###Story1 Ratings###\n**Overall Quality w.r.t. Prompt**: \n\n###Story2 Ratings###\n**Overall Quality w.r.t. Prompt**: \n\n###Explanations###:"


HANNA_SIMPLE_RATE_DOUBLE_ESSAY_PROMPT_TEMPLATE="Based on the following six categories: 1. Relevance. 2. Coherence. 3. Empathy. 4. Surprise. 5. Engagement. 6. Complexity, evaluate the following two stories by assigning an integer score (from 1 to 5) to each category. Higher score means better.\nThe initial premise of story is: {}\nStory1: {}\n Story2: {}\n\nIn your response, please use the following format strictly and no need for any extra explanations: \nStory1\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \nStory2\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \n"

HANNA_RATE_DOUBLE_ESSAY_PROMPT_TEMPLATE="Based on the following six categories: 1. Relevance (how well the story matches its prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following two stories by assigning an integer score (from 1 to 5) to each category. Higher score means better.\n\nThe initial premise of story is: {}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format strictly and no need for any extra explanations: \nStory1\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \n\nStory2\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \n"

HANNA_ANALYZE_RATE_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Based on the following six attributes:\n1. Relevance (how well the story matches the prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following two stories by first providing an analysis, and then assigning an integer score (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format strictly:\n\n###Analysis###:\n\n###Story1 Ratings###\n**Relevance**: \n**Coherence**: \n**Empathy**: \n**Surprise**: \n**Engagement**: \n**Complexity**: \n\n###Story2 Ratings###\n**Relevance**: \n**Coherence**: \n**Empathy**: \n**Surprise**: \n**Engagement**: \n**Complexity**: \n"

HANNA_RATE_EXPLAIN_DOUBLE_ESSAY_PROMPT_TEMPLATE = "Based on the following six attributes:\n1. Relevance (how well the story matches its prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following two stories by assigning an integer score (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt of story is: {}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format strictly:\n\n###Story1 Ratings###\n**Relevance**: \n**Coherence**: \n**Empathy**: \n**Surprise**: \n**Engagement**: \n**Complexity**: \n\n###Story2 Ratings###\n**Relevance**: \n**Coherence**: \n**Empathy**: \n**Surprise**: \n**Engagement**: \n**Complexity**: \n\n###Explanations###:"

HANNA_SIMPLE_RATE_SINGLE_ESSAY_PROMPT_TEMPLATE="Based on the following six categories: 1. Relevance. 2. Coherence. 3. Empathy. 4. Surprise. 5. Engagement. 6. Complexity, evaluate the following story by assigning an integer score (from 1 to 5) to each category. Higher score means better.\nThe initial premise of story is: {}\nStory: {}\n\nIn your response, please use the following example format strictly and no need for any extra explanations:\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \n"

HANNA_RATE_SINGLE_ESSAY_PROMPT_TEMPLATE="Based on the following six categories: 1. Relevance (how well the story matches its prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following story by assigning an integer score (from 1 to 5) to each category. Higher score means better.\nThe initial prompt of story is: {}\nStory: {}\n\nIn your response, please use the following example format strictly and no need for any extra explanations:\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \n"

HANNA_ANALYZE_RATE_SINGLE_ESSAY_PROMPT_TEMPLATE="Based on the following six attributes:\n1. Relevance (how well the story matches its prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following story regarding the given evaluation criteria concisely, and then give an integer rating (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt: {}\n\nThe story: {}\n\nIn your response, please use the following format:\nAnalysis:\n###Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n"

HANNA_SIMPLE_ANALYZE_RATE_SINGLE_ESSAY_PROMPT_TEMPLATE="Based on the following six attributes:\n1. Relevance.\n2. Coherence.\n3. Empathy.\n4. Surprise.\n5. Engagement.\n6. Complexity.\nEvaluate the following story regarding the given evaluation criteria concisely, and then give an integer rating (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt: {}\n\nThe story: {}\n\nIn your response, please use the following format:\nAnalysis:\n###Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n"

HANNA_RATE_EXPLAIN_SINGLE_ESSAY_PROMPT_TEMPLATE="Based on the following six attributes:\n1. Relevance (how well the story matches its prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nGive an integer rating (from 1 to 5, higher means better) to each attribute of the following story first, and then give the explanation of the ratings.\n\nThe initial prompt: {}\n\nThe story: {}\n\nIn your response, please use the following format:\n###Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n\n###Explanations###:"


QUARREL_PREMISE = "You will collaborate to create a story. The general setting: A Quarrel between two good friends about Iron Man."

IBRUSIA_PREMISE = "You will collaborate to create a story. The general setting: The state of Ibrusia is coming to a desperate and dangerous situation as the Hosso Union approaches its capital, Zaragoza."

ECONOMY_PREMISE = "You will collaborate to create a story. The general setting: The state of Gurata is coming to a huge economic recession. People are in panic and streets are in turmoil."