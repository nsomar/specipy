#import <Kiwi/Kiwi.h>

SPEC_BEGIN(SomeTest1Spec)

describe(@"The first describe", ^{

  context(@"first context", ^{

    it(@"has this test", ^{

    });

    it(@"and a second test", ^{

    });

    context(@"inner context", ^{

        it(@"has this an inner test", ^{

        });

        it(@"and a second inner test", ^{

        });

  });

  });

  context(@"second context", ^{

    it(@"has this othertest", ^{

    });

  });

});

describe(@"The second describe", ^{
  context(@"second descibe context", ^{

    it(@"has this other test", ^{

    });

    it(@"and another test", ^{

    });

  });

});

SPEC_END