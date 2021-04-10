# NoteBook 1
# SHAZZAD  HOSSEN
#_________________________________



#include<stdio.h>
int main()

{

    int pass1=1234,i,pass2;


    for(i=1; i<=5; i++)
    {
        printf("\n\nPlease Enter Password: ");
        scanf("%d",&pass2);

        if(pass1==pass2)
        {
            
            printf("Correct!");
            return 0;

        }

        else
        {
            
            if((5-i)==0)printf("\n\nIncorrect Password! No attempts left");
            else
            printf("\n\nIncorrect Password! %d attempts left",5-i);

        }



    }







    return 0;
}
