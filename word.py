

word1 = input("글자를 입력하세요.")


if (len(word1)==3):
    
        while True:
            word2 = input("글자를 입력하세요.")

            if(len(word2)==3) and (word2[0]==word1[2]):
            
                print("정답입니다.")
            
            else:
                
                    print("오답입니다.",word2[0],word1[2])
            
            break
        
else:
    
        print("오답입니다.")
    
    
print("게임이 끝났습니다.")
    # while True:
    #     word2 = input("글자를 입력하세요.")

    # if(len(word2)==3) and (word2[0]==word1[2]):
    #     {
    #         print("정답입니다.")
    #     }
    # else:
    #     {
    #         print("오답입니다.")
    #     } 
    #     break