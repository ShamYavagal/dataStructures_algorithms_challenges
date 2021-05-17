import re

#inputlines = "Wait a minute. Wait a minute, Doc. Are you telling me that you built a time machine out of a DeLorean?"

inputlines = "Please let me know if you are available during one of the below time slots so we can answer any questions you might have.  I'm happy to send over additional options if these proposed time slots do not align with your availability.  Please don't hesitate to shoot over any questions beforehand if you'd like.  We look forward to hearing your feedback.  "


def sentences(inputLines):
    
    inputLines = re.sub("[^A-Za-z0-9.']+", ' ', inputLines).lower()
    
    #inputLines = inputLines.strip(',').strip('?').lower()
        
    sentences_dict = {}
    sentences_list = inputLines.split('.') #This results in the input being split into a list with elements of that list as each sentence.
    
    for index, sentence in enumerate(sentences_list):
        index_num = index + 1                            #Just using 1 for naming convention, instead of 0.
        #word_list = [word for word in sentence.split()] #split returns a list
        word_list = sentence.split()
        sentences_dict[index_num] = word_list
            
    word_dict = {}
    for sentence_list_num, list_of_words in sentences_dict.items(): 
        
        for word in list_of_words:
            word_dict[word] = [0] if not word_dict.get(word) else word_dict[word]
            word_dict[word][0] += 1
            
    non_duplicate_words = set(inputLines.split())

    for each_word in non_duplicate_words:     
        each_word = each_word.strip('.')  
        for num, each_sent in enumerate(sentences_list):
            sentence_num = num + 1
            if each_word in each_sent.split():
                each_count = each_sent.split().count(each_word)
                if each_count > 1:
                    for each in range(each_count):
                        word_dict[each_word].append(sentence_num)
                else:
                    word_dict[each_word].append(sentence_num)
    
    final_string = ''
    for key, value in sorted(word_dict.items()):

        final_string += "\t\n" + str(key) + ":" + " {" + str(value[0]) + ":" + ",".join([str(each) for each in value[1:]]) + "}"
        
    print(final_string)  

    return final_string
    
sentences(inputlines)
        