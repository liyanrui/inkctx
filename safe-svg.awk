BEGIN {
    "cat " svg_num_file | getline svg_count
}

# 为 id 加前缀
/id *= *"[^"]+"/ {
    $0 = gensub(/id *= *"([^"]+)"/, "id=\"lhm_" svg_count "_\\1\"", "g")
}

# 为 href 引用的 id 加前缀
/href *= *"#[^"]+"/ {
    $0 = gensub(/href *= *"#([^"]+)"/, "href=\"#lhm_" svg_count "_\\1\"", "g")
}

# 为 url 引用的 id 加前缀
/url\(#[^)]+\)/ {
    $0 = gensub(/url\(#([^)]+)\)/, "url(#lhm_" svg_count "_\\1)", "g")
}

# 输出上述修改结果，至于其他情况，则原样输出
{ print }

END {
    # svg 编号增 1 并保存到 svg_num_file
    svg_count++
    print svg_count > svg_num_file
}
