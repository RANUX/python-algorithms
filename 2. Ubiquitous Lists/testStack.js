(function(){
"use strict";
function str(s) {
    return ""+s;
}
function ՐՏ_extends(child, parent) {
    child.prototype = Object.create(parent.prototype);
    child.prototype.__base__ = parent;
    child.prototype.constructor = child;
}
function ՐՏ_Iterable(iterable) {
    var tmp;
    if (iterable.constructor === [].constructor || iterable.constructor === "".constructor || (tmp = Array.prototype.slice.call(iterable)).length) {
        return tmp || iterable;
    }
    return Object.keys(iterable);
}
function len(obj) {
    var tmp;
    if (obj.constructor === [].constructor || obj.constructor === "".constructor || (tmp = Array.prototype.slice.call(obj)).length) {
        return (tmp || obj).length;
    }
    return Object.keys(obj).length;
}
function range(start, stop, step) {
    var length, idx, range;
    if (arguments.length <= 1) {
        stop = start || 0;
        start = 0;
    }
    step = arguments[2] || 1;
    length = Math.max(Math.ceil((stop - start) / step), 0);
    idx = 0;
    range = new Array(length);
    while (idx < length) {
        range[idx++] = start;
        start += step;
    }
    return range;
}
function ՐՏ_type(obj) {
    return obj && obj.constructor && obj.constructor.name ? obj.constructor.name : Object.prototype.toString.call(obj).slice(8, -1);
}
function ՐՏ_eq(a, b) {
    var ՐՏitr9, ՐՏidx9;
    var i;
    if (a === b) {
        return true;
    }
    if (Array.isArray(a) && Array.isArray(b) || a instanceof Object && b instanceof Object) {
        if (a.constructor !== b.constructor || a.length !== b.length) {
            return false;
        }
        if (Array.isArray(a)) {
            for (i = 0; i < a.length; i++) {
                if (!ՐՏ_eq(a[i], b[i])) {
                    return false;
                }
            }
        } else {
            if (Object.keys(a).length !== Object.keys(b).length) {
                return false;
            }
            ՐՏitr9 = ՐՏ_Iterable(a);
            for (ՐՏidx9 = 0; ՐՏidx9 < ՐՏitr9.length; ՐՏidx9++) {
                i = ՐՏitr9[ՐՏidx9];
                if (!ՐՏ_eq(a[i], b[i])) {
                    return false;
                }
            }
        }
        return true;
    }
    return false;
}
class AssertionError extends Error {
    constructor (message) {
        super();
        var self = this;
        self.name = "AssertionError";
        self.message = message;
    }
}
class IndexError extends Error {
    constructor (message) {
        super();
        var self = this;
        self.name = "IndexError";
        self.message = message;
    }
}
class TypeError extends Error {
    constructor (message) {
        super();
        var self = this;
        self.name = "TypeError";
        self.message = message;
    }
}
class ValueError extends Error {
    constructor (message) {
        super();
        var self = this;
        self.name = "ValueError";
        self.message = message;
    }
}
var ՐՏ_modules = {};
ՐՏ_modules["stdlib"] = {};
ՐՏ_modules["unittest"] = {};
ՐՏ_modules["stack"] = {};
ՐՏ_modules["random"] = {};

(function(){
    var __name__ = "stdlib";
    var str;
    str = JSON.stringify;
    String.prototype.find = String.prototype.indexOf;
    String.prototype.strip = String.prototype.trim;
    String.prototype.lstrip = String.prototype.trimLeft;
    String.prototype.rstrip = String.prototype.trimRight;
    String.prototype.join = function(iterable) {
        return iterable.join(this);
    };
    String.prototype.zfill = function(size) {
        var s;
        s = this;
        while (s.length < size) {
            s = "0" + s;
        }
        return s;
    };
    function list(iterable=[]) {
        var ՐՏitr1, ՐՏidx1;
        var result, i;
        result = [];
        ՐՏitr1 = ՐՏ_Iterable(iterable);
        for (ՐՏidx1 = 0; ՐՏidx1 < ՐՏitr1.length; ՐՏidx1++) {
            i = ՐՏitr1[ՐՏidx1];
            result.append(i);
        }
        return result;
    }
    Array.prototype.append = Array.prototype.push;
    Array.prototype.find = Array.prototype.indexOf;
    Array.prototype.index = function(index) {
        var ՐՏ_1;
        var val;
        val = this.find(index);
        if ((val === (ՐՏ_1 = -1) || typeof val === "object" && ՐՏ_eq(val, ՐՏ_1))) {
            throw new ValueError(str(index) + " is not in list");
        }
        return val;
    };
    Array.prototype.insert = function(index, item) {
        this.splice(index, 0, item);
    };
    Array.prototype.pop = function(index=this.length - 1) {
        return this.splice(index, 1)[0];
    };
    Array.prototype.extend = function(array2) {
        this.push.apply(this, array2);
    };
    Array.prototype.remove = function(item) {
        var index;
        index = this.find(item);
        this.splice(index, 1);
    };
    Array.prototype.copy = function() {
        return this.slice(0);
    };
    function dict(iterable) {
        var ՐՏitr2, ՐՏidx2;
        var result, key;
        result = {};
        ՐՏitr2 = ՐՏ_Iterable(iterable);
        for (ՐՏidx2 = 0; ՐՏidx2 < ՐՏitr2.length; ՐՏidx2++) {
            key = ՐՏitr2[ՐՏidx2];
            result[key] = iterable[key];
        }
        return result;
    }
    if (ՐՏ_type(Object.getOwnPropertyNames) !== "function") {
        dict.keys = function(hash) {
            var keys;
            keys = [];
            
        for (var x in hash) {
            if (hash.hasOwnProperty(x)) {
                keys.push(x);
            }
        }
        ;
            return keys;
        };
    } else {
        dict.keys = function(hash) {
            return Object.getOwnPropertyNames(hash);
        };
    }
    dict.values = function(hash) {
        var ՐՏitr3, ՐՏidx3;
        var vals, key;
        vals = [];
        ՐՏitr3 = ՐՏ_Iterable(dict.keys(hash));
        for (ՐՏidx3 = 0; ՐՏidx3 < ՐՏitr3.length; ՐՏidx3++) {
            key = ՐՏitr3[ՐՏidx3];
            vals.append(hash[key]);
        }
        return vals;
    };
    dict.items = function(hash) {
        var ՐՏitr4, ՐՏidx4;
        var items, key;
        items = [];
        ՐՏitr4 = ՐՏ_Iterable(dict.keys(hash));
        for (ՐՏidx4 = 0; ՐՏidx4 < ՐՏitr4.length; ՐՏidx4++) {
            key = ՐՏitr4[ՐՏidx4];
            items.append([key, hash[key]]);
        }
        return items;
    };
    dict.copy = dict;
    dict.clear = function(hash) {
        var ՐՏitr5, ՐՏidx5;
        var key;
        ՐՏitr5 = ՐՏ_Iterable(dict.keys(hash));
        for (ՐՏidx5 = 0; ՐՏidx5 < ՐՏitr5.length; ՐՏidx5++) {
            key = ՐՏitr5[ՐՏidx5];
            delete hash[key];
        }
    };
    ՐՏ_modules["stdlib"]["str"] = str;

    ՐՏ_modules["stdlib"]["list"] = list;

    ՐՏ_modules["stdlib"]["dict"] = dict;
})();

(function(){
    var __name__ = "unittest";
    var assert;
    var stdlib = ՐՏ_modules["stdlib"];
    
    assert = function(result) {
        if (!result) {
            throw new AssertionError();
        }
    };
    function main() {
        var ՐՏitr6, ՐՏidx6, ՐՏitr7, ՐՏidx7;
        var num_tests, bad_tests, overall, start_time, object, obj, prop, new_obj, result, elapsed;
        num_tests = 0;
        bad_tests = 0;
        overall = "OK";
        start_time = new Date();
        ՐՏitr6 = ՐՏ_Iterable(Object.getOwnPropertyNames(global));
        for (ՐՏidx6 = 0; ՐՏidx6 < ՐՏitr6.length; ՐՏidx6++) {
            object = ՐՏitr6[ՐՏidx6];
            if (global[object] && global[object].prototype instanceof TestCase) {
                obj = new global[object]();
                ՐՏitr7 = ՐՏ_Iterable(Object.getOwnPropertyNames(obj));
                for (ՐՏidx7 = 0; ՐՏidx7 < ՐՏitr7.length; ՐՏidx7++) {
                    prop = ՐՏitr7[ՐՏidx7];
                    if (prop.slice(0, 4) === "test") {
                        ++num_tests;
                        new_obj = new global[object]();
                        if (ՐՏ_type(new_obj.setUp) === "function") {
                            new_obj.setUp();
                        }
                        try {
                            new_obj[prop]();
                            result = "ok";
                        } catch (ՐՏ_Exception) {
                            if (ՐՏ_Exception instanceof AssertionError) {
                                var e = ՐՏ_Exception;
                                result = "FAIL";
                                ++bad_tests;
                            } else {
                                throw ՐՏ_Exception;
                            }
                        }
                        console.log(prop + " (" + object + ") ... " + result);
                        if (ՐՏ_type(new_obj.tearDown) === "function") {
                            new_obj.tearDown();
                        }
                    }
                }
            }
        }
        elapsed = (new Date() - start_time) / 1e3;
        console.log("--------------------------------------------------------------");
        console.log("Ran " + str(num_tests) + " tests in " + elapsed + "s\n");
        if (bad_tests) {
            overall = "FAILED (failures=" + str(bad_tests) + ")";
        }
        console.log(overall);
    }
    class TestCase {
        constructor () {
            var self = this;
        }
        assertEqual (a, b) {
            var self = this;
            assert(deep_eq(a, b));
        }
        assertNotEqual (a, b) {
            var self = this;
            assert(!deep_eq(a, b));
        }
        assertTrue (a) {
            var self = this;
            assert(a);
        }
        assertFalse (a) {
            var self = this;
            assert(!a);
        }
        assertAlmostEqual (a, b, precision) {
            var self = this;
            var epsilon;
            epsilon = 1 / Math.pow(10, precision);
            assert(Math.abs(a - b) < epsilon);
        }
        assertNotAlmostEqual (a, b, precision) {
            var self = this;
            try {
                self.assertAlmostEqual(a, b, precision);
            } catch (ՐՏ_Exception) {
                if (ՐՏ_Exception instanceof AssertionError) {
                    return;
                } else {
                    throw ՐՏ_Exception;
                }
            }
            throw new AssertionError();
        }
        assertRaises (exception, callable) {
            var self = this;
            var args = [].slice.call(arguments, 2);
            try {
                callable(...args);
            } catch (ՐՏ_Exception) {
                if (ՐՏ_Exception instanceof exception) {
                    return;
                } else {
                    throw ՐՏ_Exception;
                }
            }
        }
    }
    ՐՏ_modules["unittest"]["assert"] = assert;

    ՐՏ_modules["unittest"]["main"] = main;

    ՐՏ_modules["unittest"]["TestCase"] = TestCase;
})();

(function(){
    var __name__ = "stack";
    class Stack {
        constructor () {
            var self = this;
            self.stack = [];
        }
        isEmpty () {
            var self = this;
            return len(self.stack) === 0;
        }
        push (v) {
            var self = this;
            self.stack.append(v);
        }
        pop () {
            var self = this;
            if (self.isEmpty()) {
                throw Exception("Stack is empty.");
            }
            return self.stack.pop();
        }
        __repr__ () {
            var self = this;
            return "stack:" + str(self.stack);
        }
    }
    ՐՏ_modules["stack"]["Stack"] = Stack;
})();

(function(){
    var __name__ = "random";
    var _$rapyd$_seed_state, _$rapyd$_get_random_byte;
    _$rapyd$_seed_state = {
        key: [],
        key_i: 0,
        key_j: 0
    };
    _$rapyd$_get_random_byte = function() {
        _$rapyd$_seed_state.key_i = (_$rapyd$_seed_state.key_i + 1) % 256;
        _$rapyd$_seed_state.key_j = (_$rapyd$_seed_state.key_j + _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i]) % 256;
        [_$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i], _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_j]] = [ _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_j], _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i] ];
        return _$rapyd$_seed_state.key[(_$rapyd$_seed_state.key[_$rapyd$_seed_state.key_i] + _$rapyd$_seed_state.key[_$rapyd$_seed_state.key_j]) % 256];
    };
    function seed(x=new Date().getTime()) {
        var i, j;
        if (typeof x === "number") {
            x = x.toString();
        } else if (typeof x !== "string") {
            throw new TypeError("unhashable type: '" + typeof x + "'");
        }
        for (i = 0; i < 256; i++) {
            _$rapyd$_seed_state.key[i] = i;
        }
        j = 0;
        for (i = 0; i < 256; i++) {
            j = (j + _$rapyd$_seed_state.key[i] + x.charCodeAt(i % x.length)) % 256;
            [_$rapyd$_seed_state.key[i], _$rapyd$_seed_state.key[j]] = [ _$rapyd$_seed_state.key[j], _$rapyd$_seed_state.key[i] ];
        }
    }
    seed();
    function random() {
        var n, m, i;
        n = 0;
        m = 1;
        for (i = 0; i < 8; i++) {
            n += _$rapyd$_get_random_byte() * m;
            m *= 256;
        }
        return n / 0x10000000000000000;
    }
    function randrange() {
        return choice(range.apply(this, arguments));
    }
    function randint(a, b) {
        return parseInt(random() * (b - a + 1) + a);
    }
    function uniform(a, b) {
        return random() * (b - a) + a;
    }
    function choice(seq) {
        if (seq.length > 0) {
            return seq[Math.floor(random() * seq.length)];
        } else {
            throw new IndexError();
        }
    }
    function shuffle(x, random_f=random) {
        var i, j;
        for (i = 0; i < x.length; i++) {
            j = Math.floor(random_f() * (i + 1));
            [x[i], x[j]] = [ x[j], x[i] ];
        }
        return x;
    }
    function sample(population, k) {
        var ՐՏitr8, ՐՏidx8;
        var x, i, j;
        x = population.slice();
        ՐՏitr8 = ՐՏ_Iterable(range(population.length - 1, population.length - k - 1, -1));
        for (ՐՏidx8 = 0; ՐՏidx8 < ՐՏitr8.length; ՐՏidx8++) {
            i = ՐՏitr8[ՐՏidx8];
            j = Math.floor(random() * (i + 1));
            [x[i], x[j]] = [ x[j], x[i] ];
        }
        return x.slice(population.length - k);
    }
    ՐՏ_modules["random"]["_$rapyd$_seed_state"] = _$rapyd$_seed_state;

    ՐՏ_modules["random"]["_$rapyd$_get_random_byte"] = _$rapyd$_get_random_byte;

    ՐՏ_modules["random"]["seed"] = seed;

    ՐՏ_modules["random"]["random"] = random;

    ՐՏ_modules["random"]["randrange"] = randrange;

    ՐՏ_modules["random"]["randint"] = randint;

    ՐՏ_modules["random"]["uniform"] = uniform;

    ՐՏ_modules["random"]["choice"] = choice;

    ՐՏ_modules["random"]["shuffle"] = shuffle;

    ՐՏ_modules["random"]["sample"] = sample;
})();

(function(){

    var __name__ = "__main__";

    var unittest = ՐՏ_modules["unittest"];
    
    var Stack = ՐՏ_modules["stack"].Stack;
    
    var random = ՐՏ_modules["random"];
    
    class TestStack extends unittest.TestCase {
        setUp () {
            var self = this;
            self.st = new Stack();
        }
        tearDown () {
            var self = this;
            self.st = null;
        }
        test_basic () {
            var self = this;
            self.assertTrue(self.st.isEmpty());
            self.st.push(99);
            self.assertFalse(self.st.isEmpty());
            self.assertEqual(99, self.st.pop());
            self.assertTrue(self.st.isEmpty());
        }
        test_stackBehavior () {
            var self = this;
            self.assertTrue(self.st.isEmpty());
            self.st.push(99);
            self.st.push(50);
            self.st.push(25);
            self.assertEqual(25, self.st.pop());
            self.assertEqual(50, self.st.pop());
            self.assertEqual(99, self.st.pop());
            self.assertTrue(self.st.isEmpty());
        }
    }
    if (__name__ === "__main__") {
        unittest.main();
    }
})();
})();
