%% b)
Aeq = [2, 3, 2, 1, 0;
    1, 1, 2, 0, 1];
c=[7; 8; 10; 0; 0];

beq = [1000; 800];

simpAlg(c, Aeq(:,1:3), beq, Aeq, beq)


%% c)
Aeq = [3, 1, 1, 0;
        1, 2, 0, 1];
c=[4; 5; 0; 0];
beq=[8; 9];

simpAlg(c, Aeq(:,1:2), beq, Aeq, beq)
