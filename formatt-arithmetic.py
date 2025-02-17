def arithmetic_arranger(problems, show_answers=False):
    if(len(problems)>5):
      raise ValueError('Error: Too many problems.')
    for li in problems:
        if '+' not in li and '-' not in li:
            raise ValueError("Error: Operator must be '+' or '-'.")
    if any(char.isalpha() for char in problems):
        raise ValueError('Error: Numbers must only contain digits.')
    aux_list=[aux.split() for aux in problems]
    for var in aux_list:
        for p in var:
            if p=='+' or p=='-':
               continue;
            elif len(p)>5:
                 raise ValueError('Error: Numbers cannot be more than four digits.')
    help_string=''
    cnt1=0
    for arg in aux_list:
        if cnt1==0:
            help_string+='  '
        else:
            help_string+='     ' 
        length=len(arg[0])-len(arg[2])
        if length<0:
            for i in range(abs(length)):
                help_string+=' '
        help_string+=arg[0]
        cnt1+=1
    help_string+='\n'
    cnt2=0
    for arg in aux_list:
        if cnt2==0:
            help_string+=''+arg[1]+' '
        else:
            help_string+='   '+arg[1]+' '
        length=len(arg[2])-len(arg[0])
        if length<0:
            for i in range(abs(length)):
                help_string+=' '
        cnt2+=1
        help_string+=arg[2]
    help_string+='\n'
    cnt3=0
    for arg in aux_list:
        if cnt3==0:
            help_string+='--'
        else:
            help_string+='   --'
        for i in range(max(len(arg[0]),len(arg[2]))):
                    help_string+='-'
        cnt3+=1
    if show_answers==False:
        problems=help_string
        return problems
    else:
        help_string+='\n'
        result=[]
        for arg in aux_list:
            if arg[1]=='+':
                result.append(int(arg[0])+int(arg[2]))
            else:
                result.append(int(arg[0])-int(arg[2]))
        for i in range(len(result)):
            result[i]=str(result[i])
        for i in range(len(result)):
           if i==0:
               help_string+=' '
           else:
               help_string+='    '
           if(len(result[i])>max(len(aux_list[i][0]),len(aux_list[i][2]))):
                help_string+=result[i]
           else:
                help_string+=' '+result[i]
        problems=help_string
        return  problems
print(f'{arithmetic_arranger(["3 + 855", "988 + 40"], True) }')