def generate_hashtag(s):
    """
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!
Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

    """
    new = s.title()
    new = ''.join(new.split())
    return False if (len(new) > 140 or len(new) == 0) else new




generate_hashtag('')#, False, 'Expected an empty string to return False')
generate_hashtag('Do We have A Hashtag')#[0], '#', 'Expeted a Hashtag (#) at the beginning.')
generate_hashtag('Codewars      ')#, '#Codewars', 'Should handle trailing whitespace.')
generate_hashtag('Codewars Is Nice')#, '#CodewarsIsNice', 'Should remove spaces.')
generate_hashtag('codewars is nice')#, '#CodewarsIsNice',
                      # 'Should capitalize first letters of words.')
generate_hashtag('CodeWars is nice')#, '#CodewarsIsNice',
                       #'Should capitalize all letters of words - all lower case but the first.')
generate_hashtag('c i n')#, '#CIN',
                       #'Should capitalize first letters of words even when single letters.')
generate_hashtag('codewars  is  nice')#, '#CodewarsIsNice',
                       #'Should deal with unnecessary middle spaces.')
generate_hashtag(
        'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat')#,
                      # False, 'Should return False if the final word is longer than 140 chars.')