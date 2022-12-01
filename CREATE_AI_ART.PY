from discoart import create

tp = 'A painting of sea cliffs in a tumultuous storm, Trending on ArtStation.'
ii='https://d2vyhzeko0lke5.cloudfront.net/2f4f6dfa5a05e078469ebe57e77b72f0.png'


ss = 100

da = create(
    text_prompts=tp,
    init_image=ii,
    skip_steps=ss,
)
