int main() 
{ 
    char str[] = "ABDEFGABEF"; 
    printf("The input string is %s n", str); 
    int len =  longestUniqueSubsttr(str); 
    printf("The length of the longest non-repeating "
           "character substring is %d", len); 
    return 0; 
} 
