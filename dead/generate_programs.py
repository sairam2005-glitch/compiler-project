import os
import random

os.makedirs("test_programs", exist_ok=True)

templates = [
"""
#include <stdio.h>
int main(){
    int a = %d;
    char b = a;
    printf("%d", b);
    return 0;
}
""",
"""
#include <stdio.h>
int main(){
    unsigned short a = 65535;
    signed char b = a;
    printf("%d", b);
    return 0;
}
""",
"""
#include <stdio.h>
int main(){
    int x = %d;
    int y = %d;
    if(x > y){
        printf("A");
    }
    return 0;
}
""",
"""
#include <stdio.h>
int main(){
    long a = 4294967295;
    signed char b = a;
    printf("%d", b);
}
""",
"""
#include <stdio.h>
int main(){
    int x;
    if(0){
        x = 5;
    }
    return 0;
}
"""
]

for i in range(1000):
    template = random.choice(templates)
    try:
        code = template % (random.randint(1,100), random.randint(1,100))
    except:
        code = template

    with open(f"test_programs/test{i}.c","w") as f:
        f.write(code)

print("Generated 1000 C programs")
