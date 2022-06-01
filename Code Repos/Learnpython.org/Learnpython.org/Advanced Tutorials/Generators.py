import random
import types
# return là trẻ về 1 giá trị của hàm còn yield là lưu tạm trạng thái các biến của hàm, nó sẽ có một tập các giá trị 
class generator_type:
    def __init__(self) -> None:
        pass
    def lottery():
        for i in range(6):
            yield random.randint(1, 40);

        yield random.randint(1,15)
    def test_lottery():
        for ran_num in lottery():
            print("number: %d" %ran_num)


    # fill in this function
    def fib():
         a, b = 1, 1
         while 1:
            yield a
            a, b = b, a + b

    # testing code
    def test():
        if type(fib()) == types.GeneratorType:
            print("Good, The fib function is a generator.")

            counter = 0
            for n in fib():
                print(n)
                counter += 1
                if counter == 10:
                    break;

class List_Comprehensions:
    def __init__(self):
        #count_words();
        #count_words2()
        pass
    def count_words(self):
        sentence="the quick brown fox jumps over the lazy dog"
        words= sentence.split();
        word_length=[];
        for word in words:
            if word != "the":
                word_length.append(len(word))
            pass;
        print(words);
        print(word_length)

    def count_words2(self):
        sentence="the quick brown fox jumps over the lazy dog"
        words= sentence.split();
        word_length= [len(word) for word in words if word!= "the"]
        print(words);
        print(word_length)
#list_Comprehensions = List_Comprehensions()
#list_Comprehensions.count_words();
#list_Comprehensions.count_words2();

class Test_lamdafunc:
    sum = lambda self,x,y : x + y
    def __init__(self):
        print (self.sum(1,9));
        pass;

    

#t_lamda_func= Test_lamdafunc();
##c= t_lamda_func.__init__()

class Multiple_Function_Arguments:
    def foo(self, f:int, s: str, t: list, *therest):
        print(f)
        print(s)
        print(t)
        print(therest)

    def bar(self, f, s, t, **options):
        if options.get("action")=="sum":
            print("alo");

#multiple_Function_Arguments=Multiple_Function_Arguments()
#multiple_Function_Arguments.foo(1,"ana", [1,2,6], 6,8,9)
#multiple_Function_Arguments.bar(1,"ana",[1,2,6], action="sum")

class Test_Set:
    #Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:
    def test(self):
        print(set("my name is Eric and Eric is my name".split()));
    def test_intersection(sefl):
        a= set([1,2,6]);
        b= set([1,9,8]);
        print(a.intersection(b))
        print(b.intersection(a))
        print(a.symmetric_difference(b))
        print(b.symmetric_difference(a))
        print(a.difference(b))
        print(b.difference(a))
        print(a.union(b))
test_set=Test_Set();
test_set.test();
test_set.test_intersection()

