// HexClusterMux — Rule 30 cellular automaton on a 6-node hexagonal ring
// in1: clock ramp (phasor~)
// out1: audio, out2: sink (OR of all nodes), out3: active node count

Param base(220, min=20, max=2000);          // base frequency in Hz
Param decay(0.9993, min=0.9, max=0.99999);  // per-sample envelope decay
Param click(0.25, min=0, max=1);            // impulse amount per tick
Param spread(0, min=0, max=1);              // random bit-flip probability

Data cell(6);
Data next(6);
Data env(6);
Data ph(6);
Data ratio(6);

History seeded(0);
History sink(0);
History count(0);

// First-sample init: seed state and just-intonation ratios
if (seeded == 0) {
    poke(cell, 1, 0);
    poke(cell, 1, 3);
    poke(ratio, 1, 0);
    poke(ratio, 9/8, 1);
    poke(ratio, 5/4, 2);
    poke(ratio, 3/2, 3);
    poke(ratio, 5/3, 4);
    poke(ratio, 2, 5);
    seeded = 1;
}

tick = delta(in1) < -0.5; // ramp wrap = clock pulse
imp = 0;

if (tick) {
    // Rule 30: new = left XOR (self OR right), ring topology
    for (i = 0; i < 6; i += 1) {
        l = peek(cell, wrap(i - 1, 0, 6));
        c = peek(cell, i);
        r = peek(cell, wrap(i + 1, 0, 6));
        poke(next, l != max(c, r), i);
    }

    s = 0;
    n = 0;
    for (i = 0; i < 6; i += 1) {
        v = peek(next, i);
        // Optional mutation: random bit flip
        if (noise() * 0.5 + 0.5 < spread * 0.1667) { v = 1 - v; }
        poke(cell, v, i);
        s = max(s, v);   // OR accumulation = sink
        n += v;
        if (v > 0) { poke(env, 1, i); } // retrigger node envelope
    }

    // Sink: if the ring dies, reseed one random node
    if (s == 0) {
        k = floor((noise() * 0.5 + 0.5) * 5.999);
        poke(cell, 1, k);
        poke(env, 1, k);
        s = 1;
        n = 1;
    }
    sink = s;
    count = n;
    imp = click;
}

// Six sine partials with squared exponential envelopes
mix = 0;
for (i = 0; i < 6; i += 1) {
    p = peek(ph, i) + base * peek(ratio, i) / samplerate;
    p = p - floor(p);
    poke(ph, p, i);
    e = peek(env, i) * decay;
    poke(env, e, i);
    mix += sin(p * twopi) * e * e;
}

out1 = mix * 0.2 + imp;
out2 = sink;
out3 = count;
