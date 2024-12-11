# Accessibility and Fluid Design in Website Development

## Introduction

While developing my website project, I was mostly interested in designing a user-friendly, fluid layout that would work for everyone who accesses the site, regardless of their device or physical abilities. The aim of this project was to ensure that the website adheres to modern web accessibility standards, allowing everyone, including people with disabilities, to have a good experience in both usage and the design display across all types of devices. This essay will discuss the process I used to develop a user-orientated interface that incorporates user accessibility and fluid design principles, thus maximizing the site’s usability and inclusivity.

## Enhancements for Accessibility and Fluid Design

Since my site’s front end looked dated and was generally not user-friendly, I decided to completely redo everything, from the design itself up to the underlying HTML structure making elements more accessible and life-like. I changed all pixel dimensions to percentages or em units so that the layout would scale gracefully across different devices. It became a flexible design, as the change from static to relative units meant it could fit without distortion on any screen size, never be too wide or narrow and correctly displaying images and text.

Regarding accessibility, I added alt text on images, giving descriptions that screen readers can understand. This helps for users with visual impairments. Additionally, ARIA roles were used to describe page structure for assistive technologies such as screen readers. The document became more readable and navigable by using semantic HTML tags. These changes were paramount in making our site look not just visually appealing, but usable overall.

## Accessibility Testing Results

I tested my website using automated tools like WAVE and manually by simulating a screen reader to ensure it adhered to accessibility standards. Initially, it failed to meet required structural elements for the visual layout of the web page, with everything originally positioned using pixelated absolute positioning. I also improved the navigation links by adding ARIA labels for more specific context, in case they are being read to a blind user.

The one thing that surprised me about this is how the smallest of design elements (such as insufficient contrast or a floating form label) can make all the difference in accessibility. Though they are small and seemingly insignificant in terms of visual design, these issues can have severe negative impacts on the experience for people using assistive technologies. From now on, I will perform some accessibility testing as early as possible in the development process to detect these issues before they become real blockers.

![web accessibility evaluation](web_accessibility_evaluation.png)

## Conclusion

To sum it all up, the process of incorporating design principles, including fluid design and accessibility, has been educational in my website project. This has created an inclusive and user-friendly interface by making a site responsive to different screen sizes, accessible to those with disabilities. The color contract and semantic HTML aspects of the accessibility testing will be embedded into my thought process for future projects — allowing me to design things that not only look good but also are universally accessible. I will make accessibility my primary concern from the start and bake these practices into my entire frontend development process. 
