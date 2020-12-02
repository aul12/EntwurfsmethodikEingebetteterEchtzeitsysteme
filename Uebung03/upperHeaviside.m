function out = upperHeaviside(in)
    out = zeros(size(in));
    out(in >= 0) = 1;
end