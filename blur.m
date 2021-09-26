A = imread('ip.jpg');
A = rgb2gray(A);

%imshow(A)
% box = imboxfilt(A,3);
%imshow(box)

% box1 = imboxfilt(A,11);
% 
% edges = box1 - box;
% imshow(edges)
% med = medfilt2(A,[10 10]);
% imshow(med)

gauss = imgaussfilt(A,3);
imshow(gauss)
