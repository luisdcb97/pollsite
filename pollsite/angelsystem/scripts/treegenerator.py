import json


def add_node(trees, node, backlog):
    if node["parent_uuid"] is None:
        trees.append(node)
        return
    stack = []
    for arvore in trees:
        stack.append(arvore)
        for curr in stack:
            if node["parent_uuid"] == curr["uuid"]:
                curr["children"].append(node)
                return
            else:
                stack.extend(curr["children"])
    else:
        backlog.append(node)
        return


def flush_backlog(trees, backlog):
    for node in backlog:
        stack = []
        added = False
        for arvore in trees:
            stack.append(arvore)
            for curr in stack:
                if node["parent_uuid"] == curr["uuid"]:
                    curr["children"].append(node)
                    # TODO replace 2 inner loops by function call and exit by
                    # return instead of break + boolean
                    added = True  # Condition to break out of outer loop
                    break
                else:
                    stack.extend(curr["children"])
            if added:
                break  # break out of outer loop
        else:
            trees.append(node)
    backlog.clear()


def strip_uuids(trees):
    stack = []
    stack.extend(trees)
    for node in stack:
        node.pop("uuid")
        node.pop("parent_uuid")
        stack.extend(node["children"])


def apply_classes(trees):
    # import pdb
    # pdb.set_trace()
    stack = []
    stack.extend(trees)
    for node in stack:
        node["stackChildren"] = True
        node["HTMLclass"] = ""
        if len(node["children"]) == 0:
            node["HTMLclass"] = "leaf"
        if node["parent_uuid"] is None:
            node["HTMLclass"] += " ancestor"
        stack.extend(node["children"])


def generate_tree(user_list):
    arvores = []
    acumulador = []
    for user in user_list:
        uuid_person = user.id
        name_person = user.name
        nick_person = user.nickname
        uuid_parent = user.angel_id
        obj = {
            "uuid": uuid_person,
            "text": {
                "name": f"{name_person}",
                # "title": f"{nick_person}" if nick_person != '""' else ''
            },
            "children": [],
            "parent_uuid": uuid_parent
        }
        add_node(arvores, obj, acumulador)
    flush_backlog(arvores, acumulador)
    apply_classes(arvores)
    strip_uuids(arvores)
    return json.dumps(arvores, ensure_ascii=False)
