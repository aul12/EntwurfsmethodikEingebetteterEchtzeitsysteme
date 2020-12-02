function out = kronDelta(in1,in2)
    out = zeros(size(in1));
    out(in1 == in2) = 1;
end