function optSol = simpAlg(f,A,b,Aeq,beq)
    tableau = [Aeq, beq;
               f', 0]
           
    while true
        lastRow = tableau(end, :);
        lastRow(sum(tableau(1:end-1, :)) == 0) = 0;
        
        [maxVal, pivotCol] = max(lastRow);
        
        if maxVal <= 0
            break; 
        end
        
        [~, pivotRow] = min(tableau(1:end-1, end) ./ tableau(1:end-1, pivotCol));
        
        tableau(pivotRow,:) = tableau(pivotRow,:) / tableau(pivotRow, pivotCol);
        
        for c=1:size(tableau, 1)
            if c ~= pivotRow
                tableau(c,:) = tableau(c,:) - tableau(c,pivotCol) * tableau(pivotRow,:);
            end
        end        
    end
    optSol = tableau(2, 1:size(A, 2))';
end