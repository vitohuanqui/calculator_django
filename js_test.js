module('magicTricks', {
    beforeEach: function() {
        var $ = django.jQuery;
        $('#qunit-fixture').append('<button class="button"></button>');
    }
});

test('removeOnClick removes button on click', function(assert) {
    var $ = django.jQuery;
    removeOnClick('.button');
    assert.equal($('.button').length === 1);
    $('.button').click();
    assert.equal($('.button').length === 0);
});

test('copyOnClick adds button on click', function(assert) {
    var $ = django.jQuery;
    copyOnClick('.button');
    assert.equal($('.button').length === 0);
    $('.button').click();
    assert.equal($('.button').length === 1);
});


test('set number', function(assert) {
    var $ = django.jQuery;
    $('.one').val(4);
    $('.second').val(4);
    assert.equal($('.one').text() === 4);
    assert.equal($('.second').text() === 4);
});

QUnit.test("set number", function (assert) {
    $('.one').val(4);
    $('.second').val(4);
    assert.ok($('.one').text() === 4);
    assert.ok($('.second').text() === 4);
});