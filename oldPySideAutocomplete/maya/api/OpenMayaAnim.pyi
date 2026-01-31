from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union
import maya


"""
# Copyright 2012 Autodesk, Inc. All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk
# license agreement provided at the time of installation or download,
# or which otherwise accompanies this software in either electronic
# or hard copy form.
"""


if False:
    from typing import Dict, List, Tuple, Union, Optional

class MAnimCurveClipboard(object):
    """
    Provides control over the animation clipboard.
    
    __init__()
    Initializes a new, empty MAnimCurveClipboard object.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def clear(*args, **kwargs):
        """
        clear() -> self
        
        Clears the clipboard.
        """
        ...
    def clipboardItems(*args, **kwargs):
        """
        clipboardItems() -> MAnimCurveClipboardItemArray
        
        Returns the clipboard items.
        """
        ...
    def set(*args, **kwargs):
        """
        set( clipboard ) -> self
        set( items ) -> self
        set( items, startTime, endTime, startUnitlessInput, endUnitlessInput, strictValidation=True ) -> self
        
        Sets the content of the clipboard.
        'items' may be either an MAnimClipboardItemArray or a sequence of MAnimClipboardItems.
        """
        ...
    __new__ : builtin_function_or_method
    
    endTime : getset_descriptor
    
    endUnitlessInput : getset_descriptor
    
    isEmpty : getset_descriptor
    
    startTime : getset_descriptor
    
    startUnitlessInput : getset_descriptor
    
    theAPIClipboard : MAnimCurveClipboard


class _MMessage(object):
    """
    Base class for message callbacks.
    """
    
    
    
    @staticmethod
    def currentCallbackId(*args, **kwargs):
        """
        currentCallbackId() -> id
        
        Returns the callback ID of the currently executing callback. If called
        outside of a callback, an invalid MCallbackId and failed status will
        be returned.
        """
        ...
    @staticmethod
    def nodeCallbacks(*args, **kwargs):
        """
        nodeCallbacks(node) -> ids
        
        Returns a list of callback IDs registered to a given node.
        
         * node (MObject) - Node to query for callbacks.
         * ids (MCallbackIdArray) - Array to store the list of callback IDs.
        """
        ...
    @staticmethod
    def removeCallback(*args, **kwargs):
        """
        removeCallback(id) -> None
        
        Removes the specified callback from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.
        
         * id (MCallbackId) - identifier of callback to be removed
        """
        ...
    @staticmethod
    def removeCallbacks(*args, **kwargs):
        """
        removeCallbacks(ids) -> None
        
        Removes all of the specified callbacks from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.
        
         * idList (MCallbackIdArray) - list of callbacks to be removed.
        """
        ...
    kDefaultAction : int
    
    kDoAction : int
    
    kDoNotDoAction : int


class MAnimCurveClipboardItemArray(object):
    """
    Array of MAnimCurveClipboardItem values.
    """
    
    
    
    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        ...
    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        ...
    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        ...
    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]
        
        Use of negative indices is not supported.
        """
        ...
    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        ...
    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]
        
        Use of negative indices is not supported.
        """
        ...
    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        ...
    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        ...
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def __len__(self) -> int:
        """
        x.__len__() <==> len(x)
        """
        ...
    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        ...
    def __repr__(self) -> str:
        """
        x.__repr__() <==> repr(x)
        """
        ...
    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        ...
    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        ...
    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y
        
        Use  of negative indices is not supported.
        """
        ...
    def __str__(self) -> str:
        """
        x.__str__() <==> str(x)
        """
        ...
    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        ...
    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        ...
    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        ...
    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        ...
    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        ...
    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        ...
    __new__ : builtin_function_or_method
    
    sizeIncrement : getset_descriptor


class MAnimControl(object):
    """
    Control over animation playback and values
    """
    
    
    
    @staticmethod
    def animationEndTime(*args, **kwargs):
        """
        animationEndTime() -> MTime
        
        Return an MTime specifying the last frame of the animation, as specified by the Maya user in the Range Slider UI.
        """
        ...
    @staticmethod
    def animationStartTime(*args, **kwargs):
        """
        animationStartTime() -> MTime
        
        Return an MTime specifying the first frame of the animation, as specified by the Maya user in the Range Slider UI.
        """
        ...
    @staticmethod
    def autoKeyMode(*args, **kwargs):
        """
        autoKeyMode() -> bool
        
        Return the autoKeyMode.
        """
        ...
    @staticmethod
    def currentTime(*args, **kwargs):
        """
        currentTime() -> MTime
        
        Return an MTime instance containing the current animation frame.
        """
        ...
    @staticmethod
    def globalInTangentType(*args, **kwargs):
        """
        globalInTangentType() -> int
        
        Return the current global in tangent type.
        """
        ...
    @staticmethod
    def globalOutTangentType(*args, **kwargs):
        """
        globalOutTangentType() -> int
        
        Return the current global out tangent type.
        """
        ...
    @staticmethod
    def isPlaying(*args, **kwargs):
        """
        isPlaying() -> bool
        
        Return a value indicating whether Maya is currently playing the animation
        """
        ...
    @staticmethod
    def isScrubbing(*args, **kwargs):
        """
        isScrubbing() -> bool
        
        Return a value indicating whether interactive scrubbing is occuring while Maya is not currently playing an animation.
        """
        ...
    @staticmethod
    def maxTime(*args, **kwargs):
        """
        maxTime() -> MTime
        
        Return an MTime specifying the last frame of the current playback time range.
        """
        ...
    @staticmethod
    def minTime(*args, **kwargs):
        """
        minTime() -> MTime
        
        Return an MTime specifying the first frame of the current playback time range.
        """
        ...
    @staticmethod
    def playBackward(*args, **kwargs):
        """
        playBackward() -> None
        
        Start playing the current animation backwards.
        """
        ...
    @staticmethod
    def playForward(*args, **kwargs):
        """
        playForward() -> None
        
        Start playing the current animation forwards.
        """
        ...
    @staticmethod
    def playbackBy(*args, **kwargs):
        """
        playbackBy() -> float
        
        Return a float specifying the increment between times viewed during the playing of the animation.
        """
        ...
    @staticmethod
    def playbackMode(*args, **kwargs):
        """
        playbackMode() -> int
        
        Return the playback mode currently in effect:
          MAnimControl.kPlaybackOnce         Play once then stop.
          MAnimControl.kPlaybackLoop         Play continuously.
          MAnimControl.kPlaybackOscillate    Play forwards, then backwards continuously.
        """
        ...
    @staticmethod
    def playbackSpeed(*args, **kwargs):
        """
        playbackSpeed() -> float
        
        Return the speed with with to play the animation.
        """
        ...
    @staticmethod
    def setAnimationEndTime(*args, **kwargs):
        """
        setAnimationEndTime(MTime) -> None
        
        Set the value of the last frame in the animation.
        """
        ...
    @staticmethod
    def setAnimationStartEndTime(*args, **kwargs):
        """
        setAnimationStartEndTime(MTime, MTime) -> None
        
        Set the values of the first and last frames in the animation.
        """
        ...
    @staticmethod
    def setAnimationStartTime(*args, **kwargs):
        """
        setAnimationStartTime(MTime) -> None
        
        Set the value of the first frame in the animation.
        """
        ...
    @staticmethod
    def setAutoKeyMode(*args, **kwargs):
        """
        setAutoKeyMode(bool) -> None
        
        Set the autoKeyMode.
        """
        ...
    @staticmethod
    def setCurrentTime(*args, **kwargs):
        """
        setMinTime(MTime) -> None
        
        Set the current animation frame.
        """
        ...
    @staticmethod
    def setGlobalInTangentType(*args, **kwargs):
        """
        setGlobalInTangentType(int) -> None
        
        Set the current global in tangent type
        """
        ...
    @staticmethod
    def setGlobalOutTangentType(*args, **kwargs):
        """
        setGlobalOutTangentType(int) -> None
        
        Set the current global out tangent type.
        """
        ...
    @staticmethod
    def setMaxTime(*args, **kwargs):
        """
        setMaxTime(MTime) -> None
        
        Set the value of the last frame of the current playback time range.
        """
        ...
    @staticmethod
    def setMinMaxTime(*args, **kwargs):
        """
        setMinMaxTime(MTime, MTime) -> None
        
        Set the values of the first and last frames of the playback time range.
        """
        ...
    @staticmethod
    def setMinTime(*args, **kwargs):
        """
        setMinTime(MTime) -> None
        
        Set the value of the first frame of the current playback time range.
        """
        ...
    @staticmethod
    def setPlaybackBy(*args, **kwargs):
        """
        setPlaybackBy(float) -> None
        
        Specify the increment between times viewed during the playing of the animation.
        """
        ...
    @staticmethod
    def setPlaybackMode(*args, **kwargs):
        """
        setPlaybackMode(int) -> None
        
        Set the current playback mode.
        """
        ...
    @staticmethod
    def setPlaybackSpeed(*args, **kwargs):
        """
        setPlaybackSpeed(float) -> None
        
        Set the desired speed factor at which the animation will play back.
        """
        ...
    @staticmethod
    def setViewMode(*args, **kwargs):
        """
        setViewMode(int) -> None
        
        Set the current viewing mode.
        Controls whether the animation is run in only the active view, or simultaneously in all views.
        """
        ...
    @staticmethod
    def setWeightedTangents(*args, **kwargs):
        """
        setWeightedTangents(bool) -> None
        
        Sets whether or not the tangents on the Anim Curve are weighted.
        """
        ...
    @staticmethod
    def stop(*args, **kwargs):
        """
        stop() -> None
        
        Stop playing the current animation.
        """
        ...
    @staticmethod
    def viewMode(*args, **kwargs):
        """
        viewMode() -> int
        
        Return the viewing mode currently in effect:
          MAnimControl.kPlaybackViewAll      Playback in all views.
          MAnimControl.kPlaybackViewActive   Playback in only the active view.
        """
        ...
    @staticmethod
    def weightedTangents(*args, **kwargs):
        """
        weightedTangents() -> bool
        
        Determine whether or not the tangents on the Anim Curve are weighted.
        """
        ...
    kPlaybackLoop : int
    
    kPlaybackOnce : int
    
    kPlaybackOscillate : int
    
    kPlaybackViewActive : int
    
    kPlaybackViewAll : int


val = MAnimControl
class _MFnBase(object):
    """
    Base class for function sets.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def hasObj(*args, **kwargs):
        """
        Returns True if the function set is compatible with the specified Maya object.
        """
        ...
    def object(*args, **kwargs):
        """
        Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none.
        """
        ...
    def setObject(*args, **kwargs):
        """
        Attaches the function set to the specified Maya object.
        """
        ...
    def type(*args, **kwargs):
        """
        Returns the type of the function set.
        """
        ...
    __new__ : builtin_function_or_method


class MAnimUtil(object):
    """
    Static class providing common animation helper methods.
    """
    
    
    
    @staticmethod
    def findAnimatablePlugs(*args, **kwargs):
        """
        findAnimatablePlugs(MSelectionList) -> MPlugArray
        
        Find the list of attributes (MPlugs) on any member of an MSelectionList
        that is animatable.
        
        In addition to normal objects, components such as mesh vertices or
        faces can be easily described on an MSelectionList, making this a
        good way to determine if parts of a shape are animatable or not.
        """
        ...
    @staticmethod
    def findAnimatedPlugs(*args, **kwargs):
        """
        findAnimatedPlugs(MObject, bool) -> MPlugArray
        findAnimatedPlugs(MDagPath, bool) -> MPlugArray
        findAnimatedPlugs(MSelectionList selectionList, bool checkParent) -> MPlugArray
        
        Find the list of attributes (MPlugs) on the input object that is animated.
        """
        ...
    @staticmethod
    def findAnimation(*args, **kwargs):
        """
        findAnimation(MPlug) -> MObjectArray
        
        Find the animCurve(s) that are animating a given attribute (MPlug).
        In most cases an attribute is animated by a single animCurve and so
        just that animCurve will be returned.  It is possible to setup a
        series of connections where an attribute is animated by more than
        one animCurve, although Maya does not currently offer a UI to do so.
        Compound attributes are not expanded to include any child attributes.
        """
        ...
    @staticmethod
    def findConstraint(*args, **kwargs):
        """
        findConstraint(Mplug) -> (MObject, MObjectArray)
        
        Find any constraint that is directly driving the specified attribute.
        If a constraint is found, this method will also find the constraint
        targets. Return false if no constraint exists on the attribute.
        
        Compound attributes are not expanded to include any child attributes.
        """
        ...
    @staticmethod
    def findSetDrivenKeyAnimation(*args, **kwargs):
        """
        findSetDrivenKeyAnimation(MPlug) -> (MObjectArray, MPlugArray)
        
        Find any driven keyframe animCurves, the blendWeighted node and the
        driver attribute(s) that are animating a given attribute (MPlug).
        Or return false if no driven keyframe exists on the attribute.
        
        A driven keyframe is similar to a regular keyframe. However, while a
        standard keyframe always has an x-axis of time in the graph editor,
        for a drivenkeyframe the user may choose any attribute
        as the x-axis of the graph editor. This attribute is called the driver.
        
        In the case where there is only one driver, the animation curve
        will be connected directly to the driven attribute. When there are
        multiple drivers, the driven keyframe animCurves feed into a
        blendWeighted node which drives the attribute.
        
        Compound attributes are not expanded to include any child attributes.
        """
        ...
    @staticmethod
    def isAnimated(*args, **kwargs):
        """
        isAnimated(MObject, bool) -> bool
        isAnimated(MDagPath, bool) -> bool
        isAnimated(MPlug, bool) -> bool
        isAnimated(MSelectionList selectionList, bool checkParent) -> bool
        
        Determine whether or not an MObject is animated.
        If the MObject is a hierarchical object (such as a dag node) then
        you may also specify whether or not the input object's parents are examined.
        """
        ...


class MAnimCurveClipboardItem(object):
    """
    This class provides a wrapper for a clipboard item.
    
    __init__()
    Initializes a new, empty MAnimCurveClipboardItem object.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def animCurveType(*args, **kwargs):
        """
        animCurveType() -> MFnAnimCurve.AnimCurveType
        
        Returns the type of the item's anim curve.
        """
        ...
    def getAddressingInfo(*args, **kwargs):
        """
        getAddressingInfo() -> (unsigned int, unsigned int, unsigned int)
        
        Returns the addressing information for this clipboard item
        as (rowCount, childCount, attributeCount).
        """
        ...
    def setAddressingInfo(*args, **kwargs):
        """
        setAddressingInfo(rowCount, childCount, attributeCount) -> self
        
        Sets the addressing information for this clipboard item.
        """
        ...
    def setAnimCurve(*args, **kwargs):
        """
        setAnimCurve(object) -> self
        
        Sets the anim curve MObject.
        """
        ...
    def setNameInfo(*args, **kwargs):
        """
        setNameInfo(nodeName, fullName, leafName) -> self
        
        Sets the name information for this clipboard item.
        """
        ...
    __new__ : builtin_function_or_method
    
    animCurve : getset_descriptor
    
    fullAttributeName : getset_descriptor
    
    leafAttributeName : getset_descriptor
    
    nodeName : getset_descriptor


class MAnimCurveChange(object):
    """
    Anim curve change cache.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def redoIt(*args, **kwargs):
        """
        Redo all of the Anim Curve changes in this cache.
        """
        ...
    def undoIt(*args, **kwargs):
        """
        Undo all of the Anim Curve changes in this cache.
        """
        ...
    __new__ : builtin_function_or_method


class _MFnDependencyNode(_MFnBase):
    """
    Function set for operating on dependency nodes.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def absoluteName(*args, **kwargs):
        """
        Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).
        """
        ...
    def addAttribute(*args, **kwargs):
        """
        Adds a new dynamic attribute to the node.
        """
        ...
    def addExternalContentForFileAttr(*args, **kwargs):
        """
        Adds content info to the specified table from a file path attribute.
        """
        ...
    def affectsAnimation(*args, **kwargs):
        """
        Returns true if the changes to the node may affect animation.
        """
        ...
    def attribute(*args, **kwargs):
        """
        Returns an attribute of the node, given either its index or name.
        """
        ...
    def attributeClass(*args, **kwargs):
        """
        Returns the class of the specified attribute.
        """
        ...
    def attributeCount(*args, **kwargs):
        """
        Returns the number of attributes on the node.
        """
        ...
    def canBeWritten(*args, **kwargs):
        """
        Returns true if the node will be written to file.
        """
        ...
    def create(*args, **kwargs):
        """
        Creates a new node of the given type.
        """
        ...
    def dgCallbackIds(*args, **kwargs):
        """
        Returns DG timing information for a specific callback type, broken down by callbackId.
        """
        ...
    def dgCallbacks(*args, **kwargs):
        """
        Returns DG timing information broken down by callback type.
        """
        ...
    def dgTimer(*args, **kwargs):
        """
        Returns a specific DG timer metric for a given timer type.
        """
        ...
    def dgTimerOff(*args, **kwargs):
        """
        Turns DG timing off for this node.
        """
        ...
    def dgTimerOn(*args, **kwargs):
        """
        Turns DG timing on for this node.
        """
        ...
    def dgTimerQueryState(*args, **kwargs):
        """
        Returns the current DG timer state for this node.
        """
        ...
    def dgTimerReset(*args, **kwargs):
        """
        Resets all DG timers for this node.
        """
        ...
    def findAlias(*args, **kwargs):
        """
        Returns the attribute which has the given alias.
        """
        ...
    def findPlug(*args, **kwargs):
        """
        Returns a plug for the given attribute.
        """
        ...
    def getAffectedAttributes(*args, **kwargs):
        """
        Returns all of the attributes which are affected by the specified attribute.
        """
        ...
    def getAffectingAttributes(*args, **kwargs):
        """
        Returns all of the attributes which affect the specified attribute.
        """
        ...
    def getAliasAttr(*args, **kwargs):
        """
        Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases.
        """
        ...
    def getAliasList(*args, **kwargs):
        """
        Returns all of the node's attribute aliases.
        """
        ...
    def getConnections(*args, **kwargs):
        """
        Returns all the plugs which are connected to attributes of this node.
        """
        ...
    def getExternalContent(*args, **kwargs):
        """
        Gets the external content (files) that this node depends on.
        """
        ...
    def hasAttribute(*args, **kwargs):
        """
        Returns True if the node has an attribute with the given name.
        """
        ...
    def hasUniqueName(*args, **kwargs):
        """
        Returns True if the node's name is unique.
        """
        ...
    def isFlagSet(*args, **kwargs):
        """
        Returns the state of the specified node flag.
        """
        ...
    def isNewAttribute(*args, **kwargs):
        """
        Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files.
        """
        ...
    def isTrackingEdits(*args, **kwargs):
        """
        Returns True if the node is referenced or in an assembly that is tracking edits.
        """
        ...
    def name(*args, **kwargs):
        """
        Returns the node's name.
        """
        ...
    def plugsAlias(*args, **kwargs):
        """
        Returns the alias for a plug's attribute.
        """
        ...
    def removeAttribute(*args, **kwargs):
        """
        Removes a dynamic attribute from the node.
        """
        ...
    def reorderedAttribute(*args, **kwargs):
        """
        Returns one of the node's attribute, based on the order in which they are written to file.
        """
        ...
    def setAffectsAnimation(*args, **kwargs):
        """
        Specifies that modifications to a node could potentially affect the animation.
        """
        ...
    def setAlias(*args, **kwargs):
        """
        Adds or removes an attribute alias.
        """
        ...
    def setDoNotWrite(*args, **kwargs):
        """
        Used to prevent the node from being written to file.
        """
        ...
    def setExternalContent(*args, **kwargs):
        """
        Changes the location of external content.
        """
        ...
    def setExternalContentForFileAttr(*args, **kwargs):
        """
        Sets content info in the specified attribute from the table.
        """
        ...
    def setFlag(*args, **kwargs):
        """
        Sets the state of the specified node flag.
        """
        ...
    def setName(*args, **kwargs):
        """
        Sets the node's name.
        """
        ...
    def setUuid(*args, **kwargs):
        """
        Sets the node's UUID.
        """
        ...
    def userNode(*args, **kwargs):
        """
        Returns the MPxNode object for a plugin node.
        """
        ...
    def uuid(*args, **kwargs):
        """
        Returns the node's UUID.
        """
        ...
    @staticmethod
    def allocateFlag(*args, **kwargs):
        """
        Allocates a flag on all nodes for use by the named plugin and returns the flag's index.
        """
        ...
    @staticmethod
    def classification(*args, **kwargs):
        """
        Returns the classification string for the named node type.
        """
        ...
    @staticmethod
    def deallocateAllFlags(*args, **kwargs):
        """
        Deallocates all node flags which are currently allocated to the named plugin.
        """
        ...
    @staticmethod
    def deallocateFlag(*args, **kwargs):
        """
        Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag().
        """
        ...
    __new__ : builtin_function_or_method
    
    isDefaultNode : getset_descriptor
    
    isFromReferencedFile : getset_descriptor
    
    isLocked : getset_descriptor
    
    isShared : getset_descriptor
    
    kExtensionAttr : int
    
    kInvalidAttr : int
    
    kLocalDynamicAttr : int
    
    kNormalAttr : int
    
    kTimerInvalidState : int
    
    kTimerMetric_callback : int
    
    kTimerMetric_callbackNotViaAPI : int
    
    kTimerMetric_callbackViaAPI : int
    
    kTimerMetric_compute : int
    
    kTimerMetric_computeDuringCallback : int
    
    kTimerMetric_computeNotDuringCallback : int
    
    kTimerMetric_dirty : int
    
    kTimerMetric_draw : int
    
    kTimerMetric_fetch : int
    
    kTimerMetrics : int
    
    kTimerOff : int
    
    kTimerOn : int
    
    kTimerType_count : int
    
    kTimerType_inclusive : int
    
    kTimerType_self : int
    
    kTimerTypes : int
    
    kTimerUninitialized : int
    
    namespace : getset_descriptor
    
    pluginName : getset_descriptor
    
    typeId : getset_descriptor
    
    typeName : getset_descriptor


class MAnimMessage(_MMessage):
    """
    Class used to register callbacks for anim related messages.
    """
    
    
    
    @staticmethod
    def addAnimCurveEditedCallback(*args, **kwargs):
        """
        addAnimCurveEditedCallback(function, clientData=None) -> id
        
        This method registers a callback that is called whenever an
        AnimCurve is edited.
        
         * function - callable which will be passed a MObjectArray object containing
           an array of AnimCurves which have been edited, and the clientData object
         * clientData - User defined data passed to the callback function
        
         * return: Identifier used for removing the callback.
        """
        ...
    @staticmethod
    def addAnimKeyframeEditCheckCallback(*args, **kwargs):
        """
        addAnimKeyframeEditCheckCallback(function, clientData=None) -> id
        
        This method registers a callback that is used by the setKeyframe command
        to allow a user to consider the set keyframe request and cancel it if
        needed. The callback method should return False to abort the keyframe
        setting.
        
         * function - callable which will be passed a MPlug indicating the
           plug being keyframed and the clientData object.
           Return False to abort the keyframe action, otherwise return True
         * clientData - User defined data passed to the callback function
        
         * return: Identifier used for removing the callback.
        """
        ...
    @staticmethod
    def addAnimKeyframeEditedCallback(*args, **kwargs):
        """
        addAnimKeyframeEditedCallback(function, clientData=None) -> id
        
        This method registers a callback that is called whenever an
        a group of keys are modified.  The callback is invoked once per
        atomic change to single or group of keyframes. For example, if
        a user selects a group 5 of keys and moves them 5 units in the value
        axis, then a single callback event will be invoked with a MObject
        for each of the 5 keyframes.  The MObjects can then be used in the
        MFnKeyframeDelta function set. Refer to MFnKeyframeDelta function set
        documentation for more info.
        
         * function - callable which will be passed a MObjectArray object containing
           an array of keyframes that were edited, and the clientData object
         * clientData - User defined data passed to the callback function
        
         * return: Identifier used for removing the callback.
        """
        ...
    @staticmethod
    def addDisableImplicitControlCallback(*args, **kwargs):
        """
        addDisableImplicitControlCallback(function, clientData=None) -> id
        
        This method registers a callback that is called from bakeResults
        command after baking operation is completed, if disableImplicitControl
        is enabled. One example usage of this callback is to create the anim curve
        that is used to drive Maya rigidbody's bakeSimulationIndex, which defines
        if the rigid body should take its input from anim curve or rigid body 
        simulation.
        
         * function - callable which will be passed a MPlugArray containing the baked plugs
           (they can be replaced but must have the same number of plugs), a MDGModifier used
           if bakeResults command is undone or redone and the clientData object.
         * clientData - User defined data passed to the callback function
        
         * return: Identifier used for removing the callback.
        """
        ...
    @staticmethod
    def addNodeAnimKeyframeEditedCallback(*args, **kwargs):
        """
        addNodeAnimKeyframeEditedCallback(animNode, function, clientData=None) -> id
        
        This method registers a callback that is called whenever an a
        group of keys are modified.  The callback is invoked once per
        atomic change to single or group of keyframes on the specified
        animation curve node. For example, if a user selects a group 5
        of keys and moves them 5 units in the value axis, then a single
        callback event will be invoked with a MObject for each of the 5
        keyframes.  The MObjects can then be used in the MFnKeyframeDelta
        function set. Refer to MFnKeyframeDelta function set documentation
        for more info.
        
         * animNode (MObject) - the param curve node you want to watch.
         * function - callable which will be passed a MObject indicating the
           edited animation node, a MObjectArray containing an array of keyframes
           that were edited and the clientData object.
         * clientData - User defined data passed to the callback function
        
         * return: Identifier used for removing the callback.
        """
        ...
    @staticmethod
    def addPostBakeResultsCallback(*args, **kwargs):
        """
        addPostBakeResultsCallback(function, clientData=None) -> id
        
        This method registers a callback that is called from bakeResults
        command after the simulation. If the plugArray is replaced, then
        the anim curves created from baking will be connected to the new
        plugs.
        
         * function - callable which will be passed a MPlugArray containing the baked
           plugs to which the resulting anim curves will be connected (they can be
           replaced but must have the same number of plugs),a MDGModifier used if
           bakeResults command is undone or redone and the clientData object.
         * clientData - User defined data passed to the callback function
        
         * return: Identifier used for removing the callback.
        """
        ...
    @staticmethod
    def addPreBakeResultsCallback(*args, **kwargs):
        """
        addPreBakeResultsCallback(function, clientData=None) -> id
        
        This method registers a callback that is called from bakeResults
        command before the simulation. One example usage is handle the runup to
        the first frame in a dynamic system. If plugArray is set to zero
        length in the callback, the baking will be aborted.
        
         * function - callable which will be passed a MPlugArray containing the plugs
           to be baked (they can be replaced but must have the same number of plugs)
           ,a MDGModifier used if bakeResults command is undone or redone and the
           clientData object.
         * clientData - User defined data passed to the callback function
        
         * return: Identifier used for removing the callback.
        """
        ...
    @staticmethod
    def flushAnimKeyframeEditedCallbacks(*args, **kwargs):
        """
        flushAnimKeyframeEditedCallbacks() -> None
        
        Animation keyframe edited callbacks are queued to only be issued on an
        idle event. There may be times when it is desired to issue the callback
        at a specific time. This method provides this functionality. It will
        flush all animation keyframe edited callbacks and force them to issue
        their callbacks with the data contained within.
        """
        ...


class MFnGeometryFilter(_MFnDependencyNode):
    """
    Function set for operating on geometryFilter nodes.
    geometryFilter is the abstract node type from which all
    deformer node types derive.
    
    __init__()
    Initializes a new, empty MFnGeometryFilter functionset.
    
    __init__(MObject)
    Initializes a new MFnGeometryFilter functionset and attaches it
    to a geometryFilter node.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def getInputGeometry(*args, **kwargs):
        """
        getInputGeometry() -> MObjectArray
        
        Returns the DAG nodes which provide input geometry to the deformer.
        These are found by traversing the graph to find upstream shape nodes.
        It is possible for there to be nodes in between the shape and the
        deformer so that the returned shape may have a different topology or
        tweaks then the input data to the deformer. If the actual input
        geometry data for the deformer is required, this information can be
        accessed by using MPlug::getValue() to query the inputGeometry
        attribute on the deformer.
        """
        ...
    def getOutputGeometry(*args, **kwargs):
        """
        getOutputGeometry() -> MObjectArray
        
        Returns the DAG nodes which receive output geometry from the deformer.
        """
        ...
    def getPathAtIndex(*args, **kwargs):
        """
        getPathAtIndex(plugIndex) -> MDagPath
        
        Returns the DAG path of the specified output geometry.
        
        * plugIndex (unsigned int) - Plug index of the desired geometry.
        """
        ...
    def groupIdAtIndex(*args, **kwargs):
        """
        groupIdAtIndex(plugIndex) -> long
        
        Returns the groupId associated with the specified geometry.
        
        * plugIndex (unsigned int) - Plug index of the desired geometry.
        """
        ...
    def indexForGroupId(*args, **kwargs):
        """
        indexForGroupId(groupId) -> plugIndex
        
        Returns the plug index of the geometry associated with the specified groupId.
        
        * groupId (unsigned int) - groupId of the desired geometry.
        """
        ...
    def indexForOutputConnection(*args, **kwargs):
        """
        indexForOutputConnection(connIndex) -> plugIndex
        
        Returns the plug index corresponding to a connection index. The
        connection index is the contiguous (physical) index of the output
        connection, ranging from 0 to numOutputConnections()-1. The plug
        index is the sparse (logical) index of the connection.
        
        * connIndex (unsigned int) - Connection index of the desired geometry.
        """
        ...
    def indexForOutputShape(*args, **kwargs):
        """
        indexForOutputShape(shape) -> plugIndex
        
        Returns the plug index for the specified output shape.
        
        * shape (MObject) - Shape for which the plug index is requested.
        """
        ...
    def inputShapeAtIndex(*args, **kwargs):
        """
        inputShapeAtIndex(plugIndex) -> MObject
        
        Returns the input shape corresponding to the plug index.
        
        * plugIndex (unsigned int) - Plug index of the desired shape.
        """
        ...
    def numOutputConnections(*args, **kwargs):
        """
        numOutputConnections() -> long
        
        Returns the number of output geometries connected to this node. This
        is typically equal to the number of input geometries unless an input
        or output geometry has been deleted, or a connection to an input or
        output geometry has been broken.
        
        This method is useful in conjunction with indexForOutputConnection()
        to iterate through the affected objects.
        """
        ...
    def outputShapeAtIndex(*args, **kwargs):
        """
        outputShapeAtIndex(index) -> MObject
        
        Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject.
        """
        ...
    __new__ : builtin_function_or_method
    
    deformerSet : getset_descriptor
    
    envelope : getset_descriptor


class MFnAnimCurve(_MFnDependencyNode):
    """
    Function set for operations on anim curves.
    
    __init__()
    Initializes a new, empty MFnAnimCurve object.
    
    __init__(MObject object)
    Initializes a new MFnAnimCurve and attaches it
    to an animCurve object.
    
    __init__(MPlug plug)
    Initializes a new MFnAnimCurve and attaches it
    to the single animCurve node connected to the given MPlug.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def addKey(*args, **kwargs):
        """
        addKey(at, value, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, change=None) -> unsigned int
        
        Adds a new key with the given value at the specified time.
        at and value can both be either MTime or double,depending on what is appropriate for the animCurve type.
        change is an optional MAnimCurveChange.
        """
        ...
    def addKeys(*args, **kwargs):
        """
        addKeys(times, values, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, keepExistingKeys=False, change=None) -> self
        
        Add a set of new keys with the given corresponding values and tangent typesat the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU.
        """
        ...
    def addKeysWithTangents(*args, **kwargs):
        """
        addKeysWithTangents(times, values, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, tangentInTypeArray=None, tangentOutTypeArray=None, tangentInXArray=None, tangentInYArray=None, tangentOutXArray=None, tangentOutYArray=None, tangentsLockedArray=None, weightsLockedArray=None, convertUnits=True, keepExistingKeys=False, change=None) -> self
        
        Add a set of new keys with the given corresponding values, tangent types and tangents at the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU.
        """
        ...
    def create(*args, **kwargs):
        """
        create(node, attribute, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
        create(plug, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
        create(animCurveType [, modifier] ) -> MObject
        
        Creates a new animCurve node.
        If node and attribute (MObject) are supplied, the animCurvewill be connected to the given attribute on the given node.
        If plug (MPlug) is supplied, the animCurvewill be connected to the given plug.
        modifier is an optional MDGModifier which can be used to later undo the operation.
        animCurveType specifies the type of animCurve to create. Valid values are:
        kAnimCurveTA            Time to Angular
        kAnimCurveTL            Time to Linear
        kAnimCurveTT            Time to Time
        kAnimCurveTU            Time to Unitless
        kAnimCurveUA            Unitless to Angular
        kAnimCurveUL            Unitless to Linear
        kAnimCurveUT            Unitless to Time
        kAnimCurveUU            Unitless to Unitless
        kAnimCurveUnknown       Unknown type
        """
        ...
    def evaluate(*args, **kwargs):
        """
        evaluate(at) -> value
        
        Evalutes the curve.
        For curves of type kAnimCurveTA, kAnimCurveTL and kAnimCurveTU,the at parameter is an MTime, otherwise it is a double.
        For curves of type kAnimCurveTT and kAnimCurveUT,the value is an MTime, otherwise it is a double.
        """
        ...
    def find(*args, **kwargs):
        """
        find(at) -> unsigned int
        
        Determines the index of the key which is set at the specifiedMTime (time-input curves) or double (unitless-input curves).
        Returns None if the key is not found.
        """
        ...
    def findClosest(*args, **kwargs):
        """
        findClosest(at) -> unsigned int
        
        Determines the index of the key which is set at theMTime (time-input curves) or double (unitless-input curves)closest to the specified time.
        """
        ...
    def getTangentAngleWeight(*args, **kwargs):
        """
        getTangentAngleWeight(index, isInTangent) -> (MAngle,double)
        
        Determines the angle and weight of the in- or out-tangent to the curvefor the key at the specified index
        """
        ...
    def getTangentXY(*args, **kwargs):
        """
        getTangentXY(index, isInTangent) -> (x,y)
        
        Determines the x,y value representing the vector of the in- orout-tangent (depending on the value of the isInTangent parameter) tothe curve for the key at the specified index.  The values returnedwill be in Maya's internal units (seconds for time, centimeters forlinear, radians for angles).
        """
        ...
    def inTangentType(*args, **kwargs):
        """
        inTangentType(index) -> TangentType
        
        Determines the type of the tangent to the curve entering the current key.
        """
        ...
    def input(*args, **kwargs):
        """
        input(index) -> MTime or double
        
        Determines the input (MTime for T* curves or double for U* curves) of the key at the specified index.
        """
        ...
    def insertKey(*args, **kwargs):
        """
        addKey(time, breakdown=False, change=None) -> unsigned int
        
        Inserts a new key at the specified time adjusting neighboring
        tangents to maintain curve shape. This method is the API equivalent
        to maya.cmds.setKeyframe(insert=True).
        breakdown specifies the breakdown state of the newly inserted key.
        change is an optional MAnimCurveChange.
        Returns the index of the newly inserted key.
        """
        ...
    def isBreakdown(*args, **kwargs):
        """
        isBreakdown(index) -> bool
        
        Determines whether or not a key is a breakdown.
        """
        ...
    def outTangentType(*args, **kwargs):
        """
        outTangentType(index) -> TangentType
        
        Determines the type of the tangent to the curve leaving the current key.
        """
        ...
    def remove(*args, **kwargs):
        """
        remove(index, change=None) -> self
        
        Removes the key at the specified index.
        change is an optional MAnimCurveChange.
        """
        ...
    def setAngle(*args, **kwargs):
        """
        setAngle(index, setAngle, isInTangent, change=None) -> self
        
        Sets the in- or out-angle of the tangent for the key at the given index.
        isInTangent is True to modify the inTangent or False to modify the outTangent.
        """
        ...
    def setInTangentType(*args, **kwargs):
        """
        setInTangentType(index, tangentType, change=None) -> self
        
        Sets the type of the tangent to the curve entering the key at thespecified index.
        Valid values for tangentType are:
        kTangentGlobal          Global
        kTangentFixed           Fixed
        kTangentLinear          Linear
        kTangentFlat            Flag
        kTangentSmooth          Smooth
        kTangentStep            Step
        kTangentSlow            OBSOLETE kTangentSlow should not be used. Using this tangent type may produce unwanted and unexpected results.
        kTangentFast            OBSOLETE kTangentFast should not be used. Using this tangent type may produce unwanted and unexpected results.
        kTangentClamped Clamped
        kTangentPlateau Plateau
        kTangentStepNext        StepNext
        kTangentAuto            Auto
        """
        ...
    def setInput(*args, **kwargs):
        """
        setInput(index, at, change=None) -> self
        
        Sets the input (MTime for T* curves or double for U* curves) of the key at the specified index.  This will fail ifsetting the input would require re-ordering of the keys.
        """
        ...
    def setIsBreakdown(*args, **kwargs):
        """
        setIsBreakdown(index, isBreakdown, change=None) -> self
        
        Sets the breakdown state of a key at a given index.
        """
        ...
    def setIsWeighted(*args, **kwargs):
        """
        setIsWeighted(isWeighted, change=None) -> self
        
        Sets whether or not the curve has weighted tangents.
        """
        ...
    def setOutTangentType(*args, **kwargs):
        """
        setOutTangentType(index, tangentType, change=None) -> self
        
        Sets the type of the tangent to the curve leaving the key at thespecified index.
        """
        ...
    def setPostInfinityType(*args, **kwargs):
        """
        setPostInfinityType(infinityType, change=None) -> self
        
        Sets the behaviour of the curve for the range occurring after the last key.
        """
        ...
    def setPreInfinityType(*args, **kwargs):
        """
        setPreInfinityType(infinityType, change=None) -> self
        
        Sets the behaviour of the curve for the range occurring before the first key.
        Valid values for infinityType are:
        kConstant                       Constant
        kLinear                 Linear
        kCycle                          Cycle
        kCycleRelative          Cycle relative
        kOscillate                      Oscillate
        """
        ...
    def setTangent(*args, **kwargs):
        """
        setTangent(index, xOrAngle, yOrWeight, isInTangent, change=None, convertUnits=True) -> self
        
        Sets the tangent for the key at the specified index.
        The tangent can be specified as an x/y pair, oras an MAngle and a weight.
        isInTangent is True to modify the inTangent or False to modify the outTangent.
        """
        ...
    def setTangentTypes(*args, **kwargs):
        """
        setTangentTypes(indexArray, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, change=None) -> self
        
        Sets the tangent types for multiple keys.
        """
        ...
    def setTangentsLocked(*args, **kwargs):
        """
        setTangentsLocked(index, locked, change=None) -> self
        
        Lock or unlock the tangents at the given key.
        """
        ...
    def setValue(*args, **kwargs):
        """
        setValue(index, value, change=None) -> self
        
        Sets the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U.
        """
        ...
    def setWeight(*args, **kwargs):
        """
        setWeight(index, weight, isInTangent, change=None) -> self
        
        Sets the in- or out-weight of the tangent for the key at the given index.
        isInTangent is True to modify the inTangent or False to modify the outTangent.
        """
        ...
    def setWeightsLocked(*args, **kwargs):
        """
        setWeightsLocked(index, locked, change=None) -> self
        
        Lock or unlock the weights at the given key.
        """
        ...
    def tangentsLocked(*args, **kwargs):
        """
        tangentsLocked(index) -> bool
        
        Determines whether the tangents are locked at the given key.
        """
        ...
    def timedAnimCurveTypeForPlug(*args, **kwargs):
        """
        timedAnimCurveTypeForPlug(plug) -> AnimCurveType
        
        Returns the timed animCurve type appropriate for the specified plug.
        """
        ...
    def unitlessAnimCurveTypeForPlug(*args, **kwargs):
        """
        unitlessAnimCurveTypeForPlug(plug) -> AnimCurveType
        
        Returns the unitless animCurve type appropriate for the specified plug.
        """
        ...
    def value(*args, **kwargs):
        """
        value(index) -> double
        
        Determines the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U.
        """
        ...
    def weightsLocked(*args, **kwargs):
        """
        weightsLocked(index) -> bool
        
        Determines whether the weights are locked at the given key.
        """
        ...
    __new__ : builtin_function_or_method
    
    animCurveType : getset_descriptor
    
    isStatic : getset_descriptor
    
    isTimeInput : getset_descriptor
    
    isUnitlessInput : getset_descriptor
    
    isWeighted : getset_descriptor
    
    kAnimCurveTA : int
    
    kAnimCurveTL : int
    
    kAnimCurveTT : int
    
    kAnimCurveTU : int
    
    kAnimCurveUA : int
    
    kAnimCurveUL : int
    
    kAnimCurveUT : int
    
    kAnimCurveUU : int
    
    kAnimCurveUnknown : int
    
    kConstant : int
    
    kCycle : int
    
    kCycleRelative : int
    
    kLinear : int
    
    kOscillate : int
    
    kTangentAuto : int
    
    kTangentClamped : int
    
    kTangentCustomEnd : int
    
    kTangentCustomStart : int
    
    kTangentFast : int
    
    kTangentFixed : int
    
    kTangentFlat : int
    
    kTangentGlobal : int
    
    kTangentLinear : int
    
    kTangentPlateau : int
    
    kTangentShared1 : int
    
    kTangentShared2 : int
    
    kTangentShared3 : int
    
    kTangentShared4 : int
    
    kTangentShared5 : int
    
    kTangentShared6 : int
    
    kTangentShared7 : int
    
    kTangentShared8 : int
    
    kTangentSlow : int
    
    kTangentSmooth : int
    
    kTangentStep : int
    
    kTangentStepNext : int
    
    kTangentTypeCount : int
    
    numKeys : getset_descriptor
    
    postInfinityType : getset_descriptor
    
    preInfinityType : getset_descriptor


class MFnSkinCluster(MFnGeometryFilter):
    """
    Function set for operating on skinCluster nodes.
    SkinCluster nodes are created during a smooth bindSkin. They
    store a weight per influence object for each component of the
    geometry that is deformed. Influence objects can be joints or
    any transform.
    
    Unlike most deformers, a skinCluster node can deform only a
    single geometry. Therefore, if additional geometries are added
    to the skinCluster set, they will be ignored.
    
    __init__()
    Initializes a new, empty MFnSkinCluster functionset.
    
    __init__(MObject)
    Initializes a new MFnSkinCluster functionset and attaches it to
    a skinCluster node.
    """
    
    
    
    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...
    def getBlendWeights(*args, **kwargs):
        """
        getBlendWeights(shape, components) -> MDoubleArray
        
        Returns blend weights for the specified components of the deformed
        shape. Blend weights are used to determine the blending between
        classical linear skinning and dual quaternion bases skinning on a
        per vertex basis. The returned array contains one weight per component
        in the order given by 'components'.
        
        * shape     (MDagPath) - the object being deformed by the skinCluster
        * components (MObject) - components for which weights should be returned
        """
        ...
    def getPointsAffectedByInfluence(*args, **kwargs):
        """
        getPointsAffectedByInfluence(influence) -> (MSelectionList, MDoubleArray)
        
        During deformation, the skinCluster algorithm is applied for a given
        influence object on all points in the deformer's set whose weights
        are non-zero. This returns the non-zero weights for a particular
        influence object.
        
        The return value is a tuple consisting of a selection list, which
        contains the dag path and components that are affected by the
        specified influence object, and the corresponding weights for the
        components. If no components are weighted for a specified influence
        the selection list will be empty.
        
        * influence (MDagPath) - the influence object of interest
        """
        ...
    def getWeights(*args, **kwargs):
        """
        getWeights(shape, components) -> (MDoubleArray, int)
        getWeights(shape, components, influence) -> MDoubleArray
        getWeights(shape, components, influences) -> MDoubleArray
        
        Returns the skinCluster weights of the given influence objects on
        the specified components of the deformed shape.
        
        
        If no influence index is provided then a tuple containing the weights
        and the number of influence objects will be returned.
        
        If a single influence index is provided the an array of weights will
        be returned, one per component in the same order as in 'components'.
        
        If an array of influence indices is provided an array of weights will
        be returned containing as many weights for each component as there
        are influences in the 'influenceIndices' array. The weights will be
        in component order: i.e. all of the weight values for the first
        component, followed by all the weight values for the second component,
        and so on.
        
        * shape       (MDagPath) - the object being deformed by the skinCluster
        * components   (MObject) - components to return weights for
        * influence        (int) - index of the single influence to return weights for
        * influences (MIntArray) - indices of multiple influences to return weights for
        """
        ...
    def indexForInfluenceObject(*args, **kwargs):
        """
        indexForInfluenceObject(influenceObj) -> long
        
        Returns the logical index of the matrix array attribute where the
        specified influence object is attached.
        
        * influenceObj (MObject) - influence object for which the index is requested.
        """
        ...
    def influenceObjects(*args, **kwargs):
        """
        influenceObjects() -> MDagPathArray
        
        Returns an array of paths to the influence objects for the skinCluster.
        """
        ...
    def setBlendWeights(*args, **kwargs):
        """
        setBlendWeights(shape, components, weights) -> self
        
        Sets blend weights for the specified components of the shape being
        deformed by the skinCluster. Blend weights are used to determine the
        blending between classical linear skinning and dual quaternion bases
        skinning on a per vertex basis.
        
        * shape       (MDagPath) - object being deformed by the skinCluster
        * components   (MObject) - components of 'shape' to set blend weights for
        * weights (MDoubleArray) - weights to set, one per component. If the
                                   length of this array does match the number
                                   of components provided then the lesser of
                                   the two will be used.
        """
        ...
    def setWeights(*args, **kwargs):
        """
        setWeights(shape, components, influence, weight, normalize=True, returnOldWeights=False) -> None or MDoubleArray
        setWeights(shape, components, influences, weights, normalize=True, returnOldWeights=False) -> None or MDoubleArray
        
        Sets the skinCluster weights for one or more influence objects on
        the specified components of the given shape. If 'returnOldWeights'
        is True then the old weights will be returned, otherwise None will
        be returned
        
        If only a single influence index and weight are specified then that
        weight is applied to all of the specified components. The returned
        array of old weights, if requested, will contain weights for ALL of
        the skinCluster's influence objects, not just the one specified by
        the 'influence' parameter.
        
        If arrays of influence indices and weights are provided then the
        behaviour depends upon the number of elements in the 'weights' array.
        If it's equal to the number of influences specified then each weight
        will be used for all of components for the corresponding influence
        object. If it's equal to the number of influences times the number of
        components provided, then a separate weight will be used for each
        component, with all of the weights for the first component coming
        first in the 'weights' array, followed by all of the weights for the
        second component, and so on. Within each component the weights will
        will correspond with the ordering of influence indices in the
        'influences' array. The returned old weights, if requested, will
        consist of a separate weight for
        
        The returned old weights will be ordered by influence within
        component, i.e. all of the influence weights for the first component
        will come first in the array, followed by all the weights for the
        second component, and so on.
        
        * shape       (MDagPath) - object being deformed by the skinCluster
        * components   (MObject) - the components to set weights on
        * influence        (int) - physical index of a single influence object
        * weight         (float) - single weight to be applied to all components.
        * influences (MIntArray) - physical indices of several influence objects.
        * weights (MDoubleArray) - weights to be used with several influence objects.
        * normalize       (bool) - if True, normalize weights on other influence objects
        * returnOldWeights(bool) - if True, return the old weights, otherwise return None
        """
        ...
    __new__ : builtin_function_or_method




py2dict : dict
key : str
ourdict : dict

