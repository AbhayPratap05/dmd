
/* Compiler implementation of the D programming language
 * Copyright (C) 1999-2025 by The D Language Foundation, All Rights Reserved
 * written by Walter Bright
 * https://www.digitalmars.com
 * Distributed under the Boost Software License, Version 1.0.
 * https://www.boost.org/LICENSE_1_0.txt
 * https://github.com/dlang/dmd/blob/master/src/dmd/staticassert.h
 */

#pragma once

#include "dsymbol.h"

class Expression;

class StaticAssert : public Dsymbol
{
public:
    Expression *exp;
    Expressions *msg;

    StaticAssert *syntaxCopy(Dsymbol *s) override;
    const char *kind() const override;
    void accept(Visitor *v) override { v->visit(this); }
};
