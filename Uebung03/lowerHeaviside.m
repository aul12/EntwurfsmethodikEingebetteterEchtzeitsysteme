function out = lowerHeaviside(in)
    out = zeros(size(in));
    out(in > 0) = 1;
end