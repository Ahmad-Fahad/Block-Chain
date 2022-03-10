git status
git add *

echo "Commit Options :"
echo -e "1. Project Work\n2. Excercise Problem Solving\n3. Code Archieve\n4. Code Algorithms\n5. Code Experiment Research\n6. Custom Commit " 

read option
case $option in 
1) cmmt=Project_Work;;
2) cmmt=Excercise_Problem_Solving;;
3) cmmt=Code_Archieve;;
4) cmmt=Code_Algorithms;;
5) cmmt=Code_Experiment_Research;;
6) read -p "[Commit Message ]: " cmmt;;
*) echo "Not a Valid Option"
esac



git commit -m "$cmmt"
git push