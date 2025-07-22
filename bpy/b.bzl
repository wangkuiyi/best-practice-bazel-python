def _foo_binary_impl(ctx):
    print(ctx)
    print(dir(ctx))
    print(ctx.workspace_name)

foo_binary = rule(
    implementation = _foo_binary_impl,
)
