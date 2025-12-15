def reverse_string_v1(s: str) -> str:
    lt = 0
    rt = len(s) - 1
    arr = list(s) 
    while(lt < rt):
        temp = arr[lt]
        arr[lt] = arr[rt]    
        arr[rt] = temp
        lt += 1
        rt -= 1
    return ''.join(arr)

def reverse_string_v2(s: list[str]) -> list[str]:
    s.reverse()
    return s

print(reverse_string_v1("abcd"))
print(reverse_string_v1("Hello, World"))    

print(reverse_string_v2(['a', 'b', 'c', 'd']))           
print(reverse_string_v2(list("Hello, World")))           