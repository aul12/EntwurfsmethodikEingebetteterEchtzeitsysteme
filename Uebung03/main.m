% the input as a vector of time steps
timeVector = 0:0.1:10;
outVectorU = upperHeaviside(timeVector);
%the inpunt as a time point
timePoint = 3;
outPointU = upperHeaviside(timePoint);

% the intput as a vector of time steps
timeVector = 0:0.1:10;
outVectorL = lowerHeaviside(timeVector);
%the inpunt as a time point
timePoint = 3;
outPointL = lowerHeaviside(timePoint);


% first example
in11 = 1;
in12 = 2;
out1 = kronDelta(in11,in12);
% second example
in21 = 3;
in22 = 3;
out2 = kronDelta(in21,in22);