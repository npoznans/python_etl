# dan.wiesenthal@galvanize.com
# https://github.com/danwiesenthal/Naive_Bayes_Evening_Workshop
# P(a,b) == P(b,a)
# P(a,b) == P(a|b)P(b)
# P(a|b) != P(b|a) (ordinality)
from run import started as run

def print_notes():
    print(
    '''
    if I want P(a|b), but I don't already have it
    P(a,b) = P(b,a)
    P(a|b)P(b) = P(b|a)P(a)

    P(a|b) = P(b|a)P(a) / P(b)
    posterior = (likelihood * prior) / evidence


    a test thats 99% accurate (99 specific and 99% sensitive) but only .5% in pop has it.
    What is probability that the individual actually has the condition (tests positive)?

    P(pos | cond) = (P(cond | pos) * P(cond)) / P(pos)
                  = ( P(pos | cond) * P(cond) ) /(P(pos|cond)*P(cond)+P(pos |no-cond) * P(no-cond))
                  = (.99 * .005) / (.99 * .005 + .01 * .995)
                  = .33

    another way to say this for feature sets is to say
    P(class | feature ) = (P(feature | class) * P(class))/P(feature)
                            'don't worry about the denominator for a moment'
                        = (#feat in class / # in class) * (#class / #total data points)

    For multiple features:
                          P(feature | class) * p(class)
                        = P(c, F1, F2, ... , Fn)("joint")
                        = P(c) * P(F1 | c) * P(F2 | c, F1) * P(F3 | c, F1, F2) * ...


    But if we assume independence of features given class P(Fi|c,Fj) = P(Fi|c)
                        = P(c) * P(F1|c) * P(F2|c) * P(F3|c) * ....

    Now that we can calculate the numerator for some class, we claculate it for every
    class and compare them. The largest one is the most likely class, and therefore
    the class we should predict.

        For each class c:
            pseudo_prob_data_is_in_this_class = P(c) * P(F1|c) * .. * P(Fn|c)

        prediction = the c which led to max pseudo_prob_data_is_in_this_class

    Because the denominator stays the same for all classes, so we don't have to calculate it.
    Awesome.

    Training is simply the process of couning up occurrences (all the little terms in
    "(# feat in class / # class) * (# class / # total data points)") so we can use them to predict.
    '''
    )

what = input("\n\tWhat do you want to run; bruv? > ")

if what == "print notes":
    print_notes()
elif what == "bayes":
    run()
else:
    print("I need something yo.")
