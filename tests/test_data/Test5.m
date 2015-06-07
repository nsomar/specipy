#import <Kiwi/Kiwi.h>

SPEC_BEGIN(SomeTest1Spec)

describe(@"The first describe", ^{

  context(@"first context", ^{

    it(@"has this test", ^{

    });

    it(@"and a second test", ^{

    });

  });

  context(@"second context", ^{

    it(@"has this othertest", ^{

    });

  });

});

SPEC_END